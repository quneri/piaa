def solve(n):
    best_solution = []
    best_count = float('inf')

    def find_empty_cell(board):
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    return i, j
        return None

    def can_place_square(board, x, y, size):
        if x + size > n or y + size > n:
            return False
        for i in range(x, x + size):
            for j in range(y, y + size):
                if board[i][j] != 0:
                    return False
        return True

    def place_square(board, x, y, size, value):
        for i in range(x, x + size):
            for j in range(y, y + size):
                board[i][j] = value

    empty_board = [[0] * n for _ in range(n)]
    stack = [([], empty_board)]

    while stack:
        current_solution, current_board = stack.pop()

        if len(current_solution) >= best_count:
            continue

        empty = find_empty_cell(current_board)
        if not empty:
            best_solution = current_solution
            best_count = len(current_solution)
            continue

        x, y = empty
        max_size = min(n - x, n - y, n - 1)

        for size in range(max_size, 0, -1):
            if can_place_square(current_board, x, y, size):
                new_board = [row[:] for row in current_board]
                place_square(new_board, x, y, size, 1)

                new_solution = current_solution + [(x, y, size)]
                stack.append((new_solution, new_board))

    return best_solution


n = int(input())
solution = solve(n)

print(len(solution))
for x, y, w in solution:
    print(x + 1, y + 1, w)

