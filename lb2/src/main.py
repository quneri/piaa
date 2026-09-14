from reader import read_matrix
from branch_and_bound import BranchAndBoundTSP
from amr import amr


def print_result(name, cost, path):
    print("\n" + "=" * 50)
    print(name)
    print("=" * 50)
    if path:
        print("Итоговый путь:")
        print(*path, path[0])
        print("Итоговая стоимость:", round(cost, 2))
    else:
        print("Путь не найден")


def main():
    print("Задача коммивояжера")
    print("Вариант 3")
    filename = input("Введите имя файла матрицы: ")
    graph = read_matrix(filename)

    print("\nВходная матрица весов:")
    for row in graph:
        print(row)

    start = int(input("Введите стартовую вершину: "))
    if start < 0 or start >= len(graph):
        print("Ошибка стартовой вершины")
        return

    print("Количество вершин:", len(graph))

    bb = BranchAndBoundTSP(graph, start, verbose=True)
    cost_bb, path_bb = bb.solve()
    print_result("МВиГ вариант 3 (последовательный рост пути)", cost_bb, path_bb)

    cost_amr, path_amr = amr(graph, start, verbose=True)
    print_result("АМР вариант 3", cost_amr, path_amr)


if __name__ == "__main__":
    main()
