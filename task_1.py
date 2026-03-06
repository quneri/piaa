def solve(n):
    board = [[0] * n for _ in range(n)]
    best_solution = []
    best_count = float('inf')

    solution = []
    stack = []

    def find_empty_cell():
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    return i, j
        return None

    def can_place_square(x, y, size):
        if x + size > n or y + size > n:
            return False
        for i in range(x, x + size):
            for j in range(y, y + size):
                if board[i][j] != 0:
                    return False
        return True

    def place_square(x, y, size, value):
        for i in range(x, x + size):
            for j in range(y, y + size):
                board[i][j] = value

    empty = find_empty_cell()
    if empty is None:
        return []

    x, y = empty
    max_size = min(n - x, n - y, n - 1)
    stack.append([x, y, max_size])

    while stack:
        x, y, size = stack[-1]

        if size == 0:
            stack.pop()
            if solution:
                px, py, ps = solution.pop()
                place_square(px, py, ps, 0)
            continue

        stack[-1][2] -= 1
        if len(solution) >= best_count:
            continue

        if not can_place_square(x, y, size):
            continue

        place_square(x, y, size, 1)
        solution.append((x, y, size))

        empty = find_empty_cell()
        if empty is None:
            if len(solution) < best_count:
                best_count = len(solution)
                best_solution = solution[:]

            px, py, ps = solution.pop()
            place_square(px, py, ps, 0)
        else:
            nx, ny = empty
            max_size = min(n - nx, n - ny, n - 1)
            stack.append([nx, ny, max_size])

    return best_solution


n = int(input())
solution = solve(n)

print(len(solution))
for x, y, w in solution:
    print(x + 1, y + 1, w)
