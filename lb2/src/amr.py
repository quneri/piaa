INF = float("inf")


def calculate_cost(path, graph):
    cost = 0
    for i in range(len(path) - 1):
        if graph[path[i]][path[i + 1]] == -1:
            return INF
        cost += graph[path[i]][path[i + 1]]

    if graph[path[-1]][path[0]] == -1:
        return INF
    
    cost += graph[path[-1]][path[0]]
    return cost


def initial_solution(n, start):
    return [(start + i) % n for i in range(n)]


def try_move(path, i, j):
    new_path = path[:]
    city = new_path.pop(i)
    new_path.insert(j, city)
    return new_path


def amr(graph, start, verbose=False):
    n = len(graph)
    current = initial_solution(n, start)
    current_cost = calculate_cost(current, graph)

    if verbose:
        print("\nАМР: начальное решение")
        print("Путь:", *current, current[0])
        print("Стоимость:", current_cost)

    F = n
    counter = 0
    improved = True

    while improved and counter < F:
        improved = False
        if verbose:
            print("\nАМР: итерация", counter + 1)

        for i in range(1, n):
            for j in range(1, n):
                if i == j:
                    continue

                candidate = try_move(current, i, j)
                candidate_cost = calculate_cost(candidate, graph)

                if verbose:
                    print("Проверка переноса вершины", current[i],
                          "на позицию", j,
                          "стоимость", candidate_cost)

                if candidate_cost < current_cost:
                    if verbose:
                        print("Улучшение найдено:")
                        print("Было:", current_cost, "Стало:", candidate_cost)
                    current = candidate
                    current_cost = candidate_cost
                    counter += 1
                    improved = True
                    break
            if improved:
                break

    if verbose:
        print("\nАМР завершён после", counter, "модификаций")

    return current_cost, current
