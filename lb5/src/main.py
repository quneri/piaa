from collections import deque

DEBUG = True

class Vertex:
    def __init__(self):
        # переходы по символам A, C, G, T, N
        self.next = [-1] * 5

        # суффиксная ссылка
        self.link = 0

        # конечная (терминальная) ссылка
        self.exit = -1

        # номера шаблонов, которые заканчиваются в этой вершине
        self.output = []


def debug(message):
    if DEBUG:
        print(message)


def char_id(symbol):
    if symbol == "A":
        return 0

    if symbol == "C":
        return 1

    if symbol == "G":
        return 2

    if symbol == "T":
        return 3

    return 4


def build_automaton(patterns):
    trie = [Vertex()]

    debug("\n===== ПОСТРОЕНИЕ БОРА =====\n")

    for number, pattern in enumerate(patterns, start=1):
        vertex = 0
        debug(f"Добавление шаблона №{number}: {pattern}")

        for symbol in pattern:
            index = char_id(symbol)

            if trie[vertex].next[index] == -1:
                new_vertex = len(trie)
                trie[vertex].next[index] = new_vertex
                trie.append(Vertex())

                debug(f"""Создана вершина {new_vertex}. Родитель: {vertex}. Символ: {symbol}""")

            vertex = trie[vertex].next[index]

        trie[vertex].output.append(number)

        debug(f"""Вершина {vertex}. Заканчивается шаблон №{number}""")

    debug("\n===== БОР ПОСТРОЕН =====\n")

    queue = deque()

    debug("\n==== ПОСТРОЕНИЕ ССЫЛОК ====\n")

    for symbol in range(5):
        child = trie[0].next[symbol]

        if child != -1:
            trie[child].link = 0
            queue.append(child)

            debug(f"""Вершина {child}. Суффиксная ссылка: 0""")

        else:
            trie[0].next[symbol] = 0

    while queue:
        vertex = queue.popleft()
        link = trie[vertex].link

        if trie[link].output:
            trie[vertex].exit = link

        else:
            trie[vertex].exit = trie[link].exit

        debug(f"""Вершина {vertex}. Суффиксная ссылка: {trie[vertex].link}. Конечная ссылка: {trie[vertex].exit}""")

        for symbol in range(5):
            child = trie[vertex].next[symbol]
            if child != -1:
                trie[child].link = (trie[link].next[symbol])

                queue.append(child)

                debug(f"""Создание ссылки: Вершина: {child}. link = {trie[child].link}""")

            else:
                trie[vertex].next[symbol] = (trie[link].next[symbol])

    return trie


def print_automaton(trie):
    if not DEBUG:
        return

    alphabet = "ACGTN"

    print("\n===== ОПИСАНИЕ АВТОМАТА =====\n")

    for number, vertex in enumerate(trie):
        print(f"Вершина {number}")
        print("Переходы:")

        for index, target in enumerate(vertex.next):
            print(f"  {alphabet[index]} -> {target}")

        print(f"Суффиксная ссылка: {vertex.link}")

        print(f"Конечная ссылка: {vertex.exit}")

        print(f"Выход: {vertex.output}")

        print("----------------------------")


def search(text, patterns, trie):
    result = []
    vertex = 0

    debug("\n===== ПОИСК В ТЕКСТЕ =====\n")

    for position, symbol in enumerate(text):
        index = char_id(symbol)
        vertex = trie[vertex].next[index]

        debug(f"""Позиция: {position + 1}. Символ: {symbol}. Переход в вершину: {vertex}""")
        current = vertex

        while current != -1:
            for pattern_number in trie[current].output:
                length = len(patterns[pattern_number - 1])

                start = position - length + 1
                result.append((start, position, pattern_number))

                debug(f"""Найдено совпадение:
Шаблон: {pattern_number}. Начало: {start + 1}. Конец: {position + 1}""")

            current = trie[current].exit

    return result


def remove_overlaps(matches):
    if not matches:
        return []

    debug("\n===== УДАЛЕНИЕ ПЕРЕСЕЧЕНИЙ =====\n")

    matches.sort()
    answer = []
    last_end = -1

    for start, end, number in matches:

        debug(f"""Проверяем: 
Начало: {start + 1}. Конец: {end + 1}. Шаблон: {number}""")

        if start > last_end:
            answer.append((start, end, number))
            last_end = end

            debug("Добавлено\n")

        else:
            debug("Пропущено (пересечение)\n")

    return answer


def main():
    text = input().strip()
    count = int(input())

    patterns = []

    for _ in range(count):
        patterns.append(input().strip())

    trie = build_automaton(patterns)

    print_automaton(trie)

    matches = search(text, patterns, trie)
    matches = remove_overlaps(matches)

    matches.sort(key=lambda item: (item[0], item[2]))

    print("===== ФИНАЛЬНЫЙ ОТВЕТ =====" if DEBUG else "")

    for start, _, number in matches:
        print(start + 1, number)

if __name__ == "__main__":
    main()
