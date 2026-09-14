def prefix_function(pattern):
    print("=== Построение префикс-функции ===")
    print("Шаблон:", pattern)

    n = len(pattern)
    pi = [0] * n
    j = 0

    for i in range(1, n):
        print("\nШаг i =", i)
        print("Сравниваем:", pattern[i], "и", pattern[j])

        while j > 0 and pattern[i] != pattern[j]:
            print("Несовпадение")
            print("Откат j с", j, "на", pi[j - 1])

            j = pi[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            print("Совпадение. Новое значение j =", j)

        else:
            print("Совпадения нет")

        pi[i] = j
        print("pi =", pi)

    print("\nИтоговая префикс-функция:")
    print(pi)

    return pi


def kmp_search(pattern, text):

    print("\n=== Поиск КМП ===")
    print("Текст:", text)
    print("Шаблон:", pattern)

    pi = prefix_function(pattern)
    result = []
    j = 0

    for i in range(len(text)):
        print("\nПозиция текста i =", i)
        print("Символ текста:", text[i])

        while j > 0 and text[i] != pattern[j]:
            print("Несовпадение:", text[i], "!=", pattern[j])

            print("Откат j:", j, "->", pi[j - 1])

            j = pi[j - 1]

        if text[i] == pattern[j]:
            j += 1
            print("Совпадение.", "Количество совпавших символов:", j)

        else:
            print("Совпадения нет")

        if j == len(pattern):
            position = i - len(pattern) + 1
            print("Шаблон найден.", "Начальная позиция:", position)

            result.append(position)
            print("Продолжаем поиск.", "Новый j:", pi[j - 1])

            j = pi[j - 1]

    print("\nВсе найденные позиции:")
    print(result)

    return result


pattern = input().strip()
text = input().strip()

answer = kmp_search(pattern, text)

if answer:
    print("Ответ:")
    print(",".join(map(str, answer)))
else:
    print(-1)
