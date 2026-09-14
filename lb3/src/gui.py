import tkinter as tk
from tkinter import messagebox


class GUI:
    def __init__(self, root):

        self.root = root
        self.root.title("Редакционное расстояние Вагнера-Фишера (Вариант 9а)")
        self.root.geometry("1200x850")

        input_frame = tk.Frame(root)
        input_frame.pack(pady=5)


        tk.Label(input_frame, text="Цена замены").grid(row=0, column=0)
        self.replace_entry = tk.Entry(input_frame, width=5)
        self.replace_entry.insert(0,"5")
        self.replace_entry.grid(row=0, column=1)


        tk.Label(input_frame, text="Цена вставки").grid(row=0, column=2)
        self.insert_entry = tk.Entry(input_frame, width=5)
        self.insert_entry.insert(0,"3")
        self.insert_entry.grid(row=0, column=3)


        tk.Label(input_frame, text="Цена удаления").grid(row=0, column=4)
        self.delete_entry = tk.Entry(input_frame, width=5)
        self.delete_entry.insert(0,"3")
        self.delete_entry.grid(row=0, column=5)


        tk.Label(input_frame, text="Количество нестабильных").grid(row=1, column=0)

        self.count_unstable = tk.Entry(input_frame, width=5)
        self.count_unstable.insert(0,"0")
        self.count_unstable.grid(row=1, column=1)


        tk.Label(input_frame, text="Индексы").grid(row=1, column=2)

        self.unstable_entry = tk.Entry(input_frame, width=15)
        self.unstable_entry.grid(row=1, column=3)


        tk.Label(input_frame, text="Цена сохранения").grid(row=1, column=4)

        self.save_entry = tk.Entry(input_frame, width=5)
        self.save_entry.insert(0,"4")
        self.save_entry.grid(row=1, column=5)


        tk.Label(input_frame, text="Цена особой замены").grid(row=2, column=0)

        self.special_replace_entry = tk.Entry(input_frame, width=5)
        self.special_replace_entry.insert(0,"10")
        self.special_replace_entry.grid(row=2, column=1)


        tk.Label(input_frame, text="Строка A").grid(row=3, column=0)

        self.A_entry = tk.Entry(input_frame, width=35)
        self.A_entry.grid(row=3, column=1, columnspan=4)


        tk.Label(input_frame, text="Строка B").grid(row=4, column=0)

        self.B_entry = tk.Entry(input_frame, width=35)
        self.B_entry.grid(row=4, column=1, columnspan=4)

        tk.Button(root, text="Запустить алгоритм", command=self.start).pack(pady=5)

        self.table_frame = tk.Frame(root)
        self.table_frame.pack()

        self.info = tk.Text(root, height=18, width=120)
        self.info.pack()


    def start(self):
        self.info.delete("1.0",tk.END)
        try:
            replace_cost = int(self.replace_entry.get())
            insert_cost = int(self.insert_entry.get())
            delete_cost = int(self.delete_entry.get())

            count = int(self.count_unstable.get())
            raw = self.unstable_entry.get()
            unstable = set()

            if raw:
                raw = raw.replace(","," ")
                if raw.isdigit():
                    unstable = set(map(int,raw))

                else:
                    unstable = set(map(int,raw.split()))

            if len(unstable) != count:
                if count != 0:
                    messagebox.showerror("Ошибка", "Количество индексов не совпадает")
                    return

            save_cost = int(self.save_entry.get())
            special_replace = int(self.special_replace_entry.get())

            A = self.A_entry.get()
            B = self.B_entry.get()

        except:
            messagebox.showerror("Ошибка", "Проверьте ввод")
            return

        n = len(A)
        m = len(B)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + delete_cost


        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] + insert_cost

        steps = []

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                unstable_flag = i in unstable

                if A[i - 1] == B[j - 1]:
                    if unstable_flag:
                        if A[i - 1] == "S":
                            keep = 0

                        else:
                            keep = save_cost

                    else:
                        keep = 0

                    replace = dp[i - 1][j - 1] + keep

                else:
                    if unstable_flag:
                        replace = dp[i - 1][j - 1] + special_replace

                    else:
                        replace = dp[i - 1][j - 1] + replace_cost


                delete = dp[i - 1][j] + delete_cost

                insert = dp[i][j - 1] + insert_cost

                dp[i][j] = min(replace, delete, insert)

                steps.append((i, j, A[i - 1], B[j - 1], replace, delete, insert, dp[i][j]))

        self.show_table(dp,A,B)

        self.info.insert(tk.END, "ХОД АЛГОРИТМА\n\n")

        for s in steps:
            self.info.insert(tk.END, f"A[{s[0]}]={s[2]} B[{s[1]}]={s[3]}\n")

            self.info.insert(tk.END, f"R/M={s[4]} D={s[5]} I={s[6]} -> {s[7]}\n\n")

        self.info.insert(tk.END, f"Ответ: {dp[n][m]}")


    def show_table(self,dp,A,B):
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        # верхний левый угол
        tk.Label(
            self.table_frame,
            text=" ",
            width=5,
            relief="solid"
        ).grid(row=0,column=0)

        # верхняя строка B
        for j, char in enumerate(B):
            tk.Label(
                self.table_frame,
                text=char,
                width=5,
                relief="solid"
            ).grid(
                row=0,
                column=j+2
            )

        tk.Label(
            self.table_frame,
            text="ε",
            width=5,
            relief="solid"
        ).grid(
            row=0,
            column=1
        )

        for i in range(len(dp)):
            if i == 0:
                symbol = "ε"
            else:
                symbol = A[i - 1]

            tk.Label(
                self.table_frame,
                text=symbol,
                width=5,
                relief="solid"
            ).grid(
                row=i+1,
                column=0
            )

            for j, value in enumerate(dp[i]):
                tk.Label(
                    self.table_frame,
                    text=value,
                    width=5,
                    relief="solid"
                ).grid(
                    row=i+1,
                    column=j+1
                )


root = tk.Tk()
app = GUI(root)
root.mainloop()
