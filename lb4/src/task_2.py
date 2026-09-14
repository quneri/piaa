def prefix_function(pattern):
    print("=== Построение префикс-функции ===")
    print("Шаблон:", pattern)

    n = len(pattern)
    pi = [0] * n
    j = 0

    for i in range(1, n):
        print("\nШаг i =", i)
        while j > 0 and pattern[i] != pattern[j]:
            print("Несовпадение:", pattern[i], "!=", pattern[j])

            print("Откат j:", j,"->", pi[j - 1])

            j = pi[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            print("Совпадение. j =", j)

        else:
            print("Совпадения нет")

        pi[i] = j

        print("pi =", pi)

    print("\nИтоговая таблица pi:")
    print(pi)

    return pi


def kmp_first(pattern, text):
    print("\n=== Работа КМП ===")
    print("Ищем:")
    print(pattern)

    print("В тексте:")
    print(text)

    pi = prefix_function(pattern)
    j = 0

    for i in range(len(text)):
        print("\nПозиция текста:", i)
        print("Сравнение:", text[i], "и", pattern[j])

        while j > 0 and text[i] != pattern[j]:
            print("Несовпадение")
            print("Используем pi.", "j:", j, "->", pi[j - 1])

            j = pi[j - 1]

        if text[i] == pattern[j]:
            j += 1
            print("Совпадение.", "Длина совпадения:", j)

        else:
            print("Совпадения нет")

        if j == len(pattern):
            position = i - len(pattern) + 1
            print("\nШаблон найден.", "Позиция:", position)

            return position

    print("\nШаблон не найден")
    return -1


A = input().strip()
B = input().strip()

print("\n=== Проверка циклического сдвига ===")

if len(A) != len(B):
    print("Разные длины строк.", "Циклический сдвиг невозможен.")
    print(-1)

else:
    doubled = A + A
    print("Строка A:")
    print(A)

    print("Удвоенная строка A + A:")
    print(doubled)

    answer = kmp_first(B, doubled)
    if answer >= len(A):
        print("Совпадение найдено только после границы.", "Сдвиг невозможен.")
        print(-1)

    else:
        print("\nОтвет:")
        print(answer)
