# цены обычных операций
replace_cost, insert_cost, delete_cost = map(int, input().split())

# количество нестабильных элементов
k = int(input())

# индексы нестабильных элементов
unstable_indexes = set(map(int, input().split()))

# особые цены
special_save_cost, special_replace_cost = map(int, input().split())

A = input().strip()
B = input().strip()

print("\n===== ВХОДНЫЕ ДАННЫЕ =====")
print("Обычная цена замены:", replace_cost)
print("Цена вставки:", insert_cost)
print("Цена удаления:", delete_cost)

print("Нестабильные позиции:", unstable_indexes)

print("Цена сохранения нестабильных:", special_save_cost)
print("Цена замены нестабильных:", special_replace_cost)

print("Первая строка A:", A)
print("Вторая строка B:", B)

n = len(A)
m = len(B)

# таблица dp
dp = [[0] * (m + 1) for _ in range(n + 1)]

print("\n===== ИНИЦИАЛИЗАЦИЯ ТАБЛИЦЫ =====")

# только удаления
for i in range(1, n + 1):
    dp[i][0] = dp[i-1][0] + delete_cost
    print(f"dp[{i}][0] = {dp[i][0]} " f"(удаление символа '{A[i-1]}')")

# только вставки
for j in range(1, m + 1):
    dp[0][j] = dp[0][j-1] + insert_cost
    print(f"dp[0][{j}] = {dp[0][j]} " f"(вставка символа '{B[j-1]}')")

print("\n===== ЗАПОЛНЕНИЕ ТАБЛИЦЫ =====")

# основной алгоритм Вагнера-Фишера
for i in range(1, n + 1):
    for j in range(1, m + 1):

        print("\n--------------------------------")
        print(f"Рассматриваем dp[{i}][{j}]")

        print(f"Символ A[{i}] = '{A[i-1]}'")

        print(f"Символ B[{j}] = '{B[j-1]}'")

        index = i

        # проверяем нестабильность
        unstable = index in unstable_indexes
        if unstable:
            print("Символ является нестабильным")
        else:
            print("Символ обычный")

        # сохранение / замена
        if A[i-1] == B[j-1]:
            print("Символы совпадают, рассматриваем сохранение")
            if unstable:
                if A[i-1] == "S":
                    keep_cost = 0
                    print("Особый случай: символ S")

                else:
                    keep_cost = special_save_cost
                    print("Используем особую цену сохранения:", keep_cost)

            else:
                keep_cost = 0
                print("Обычное сохранение, цена 0")

            replace = dp[i-1][j-1] + keep_cost

        else:
            print("Символы отличаются, выполняем замену")
            if unstable:
                replace = (dp[i-1][j-1] + special_replace_cost)
                print("Особая замена:", special_replace_cost)

            else:
                replace = (dp[i-1][j-1] + replace_cost)
                print("Обычная замена:", replace_cost)

        # удаление
        delete = dp[i-1][j] + delete_cost
        print("Удаление:", delete)

        # вставка
        insert = dp[i][j-1] + insert_cost
        print("Вставка:", insert)

        print("Замена/сохранение:", replace)

        dp[i][j] = min(replace, delete, insert)

        print("Выбрано минимальное значение:", dp[i][j])

print("\n===== ИТОГОВАЯ ТАБЛИЦА DP =====")

print("         ", end="")

for char in B:
    print(f"{char:4}", end="")
print()

for i in range(n + 1):
    if i == 0:
        print(" ", end=" ")
    else:
        print(A[i-1], end=" ")

    for j in range(m + 1):
        print(f"{dp[i][j]:4}", end="")
    print()

print("\n===== ОТВЕТ =====")
print("Минимальная стоимость:", dp[n][m])
