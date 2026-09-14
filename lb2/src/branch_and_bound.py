from lower_bounds import calculate_lower_bound

INF = float("inf")


class BranchAndBoundTSP:
    def __init__(self, graph, start, verbose=False):
        self.graph = graph
        self.n = len(graph)
        self.start = start
        self.best_cost = INF
        self.best_path = []
        self.verbose = verbose
        self.nodes = 0

    def initial_solution(self):
        visited = [False] * self.n
        path = [self.start]
        visited[self.start] = True
        current = self.start
        cost = 0

        print("\nПостроение начального жадного решения") if self.verbose else None

        for _ in range(self.n - 1):
            best = INF
            nxt = -1
            for city in range(self.n):
                if not visited[city] and self.graph[current][city] != -1:
                    if self.graph[current][city] < best:
                        best = self.graph[current][city]
                        nxt = city

            if nxt == -1:
                return INF, []

            if self.verbose:
                print(f"Выбрана дуга {current}->{nxt}, вес {best}")

            visited[nxt] = True
            path.append(nxt)
            cost += best
            current = nxt

        if self.graph[current][self.start] == -1:
            return INF, []

        cost += self.graph[current][self.start]
        print("Начальная верхняя граница:", cost) if self.verbose else None
        return cost, path

    def choose_next_city(self, path, visited):
        current = path[-1]
        candidates = []

        for city in range(self.n):
            if not visited[city] and self.graph[current][city] != -1:
                new_path = path + [city]
                lb = calculate_lower_bound(self.graph, new_path)
                estimate = self.graph[current][city] + lb
                candidates.append((estimate, city))

                if self.verbose:
                    print(f"Кандидат {current}->{city}: "
                          f"дуга={self.graph[current][city]}, LB={lb}, сумма={estimate}")

        candidates.sort()
        return [city for _, city in candidates]

    def dfs(self, path, visited, cost):
        self.nodes += 1
        current = path[-1]

        if self.verbose:
            print("\nИсследуем ветвь:", path, "текущая стоимость:", cost)

        if len(path) == self.n:
            if self.graph[current][self.start] == -1:
                return
            
            total = cost + self.graph[current][self.start]
            if self.verbose:
                print("Замыкание цикла:", current, "->", self.start,
                      "полная стоимость:", total)
            if total < self.best_cost:
                print("Новое лучшее решение:", total) if self.verbose else None
                self.best_cost = total
                self.best_path = path[:]
            return

        lower = cost + calculate_lower_bound(self.graph, path)
        if self.verbose:
            print("Нижняя оценка ветви:", lower,
                  "текущий рекорд:", self.best_cost)

        if lower >= self.best_cost:
            if self.verbose:
                print("Ветвь отсечена")
            return

        for city in self.choose_next_city(path, visited):
            visited[city] = True
            path.append(city)
            self.dfs(path, visited, cost + self.graph[current][city])
            path.pop()
            visited[city] = False

    def solve(self):
        cost, path = self.initial_solution()
        if path:
            self.best_cost = cost
            self.best_path = path

        visited = [False] * self.n
        visited[self.start] = True
        self.dfs([self.start], visited, 0)

        if self.verbose:
            print("\nВсего исследовано узлов дерева:", self.nodes)

        return self.best_cost, self.best_path
