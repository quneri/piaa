def solve(n):
    heights = [0] * n
    best_solution = None
    best_count = n ** 2

    stack = [(heights, [])]

    while stack:
        heights, solution = stack.pop()

        if len(solution) >= best_count:
            continue

        min_height = min(heights)
        index = heights.index(min_height)

        if min_height == n:
            best_count = len(solution)
            best_solution = solution[:]
            continue

        max_size = min(n - min_height, n - index, n - 1)
        while max_size > 0:
            flag = True
            for i in range(index, index + max_size):
                if heights[i] != min_height:
                    flag = False
                    break

            if flag:
                break
            max_size -= 1

        for size in range(max_size, 0, -1):
            new_heights = heights[:]
            for i in range(index, index + size):
                new_heights[i] += size

            new_solution = solution + [(index, min_height, size)]
            stack.append((new_heights, new_solution))
    return best_solution


n = int(input())
solution = solve(n)
print(len(solution))
for x, y, w in solution:
    print(x + 1, y + 1, w)
