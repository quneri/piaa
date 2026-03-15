def solve(n):
    if n % 2 == 0:
        half_side = n // 2
        print(4)
        for x, y in [(1, 1), (1, half_side + 1), (half_side + 1, 1), (half_side + 1, half_side + 1)]:
            print(f"{x} {y} {half_side}")
        return

    heights = [0] * n
    best_solution = None
    best_count = n * n

    stack = [[[], heights[:], [i for i in range(1, n)]]]

    while stack:
        if not stack[-1][2]:
            stack.pop()
            continue

        current_size = stack[-1][2].pop()
        current_solution_state = stack[-1][0]
        current_heights_state = stack[-1][1]

        if len(current_solution_state) + 1 >= best_count:
            continue

        new_heights = current_heights_state[:]
        current_min_height = min(new_heights)
        current_index = new_heights.index(current_min_height)

        for i in range(current_index, current_index + current_size):
            new_heights[i] += current_size

        new_solution = current_solution_state + [(current_index + 1, current_min_height + 1, current_size)]

        if min(new_heights) == n:
            if len(new_solution) < best_count:
                best_count = len(new_solution)
                best_solution = new_solution[:]
            continue

        next_min_height = min(new_heights)
        next_index = new_heights.index(next_min_height)

        next_max_width = 0
        while next_index + next_max_width < n and new_heights[next_index + next_max_width] == next_min_height:
            next_max_width += 1

        next_max_size = min(next_max_width, n - next_min_height)

        if len(new_solution) + 1 < best_count:
            stack.append([new_solution, new_heights, list(range(1, next_max_size + 1))])

    if best_solution:
        print(best_count)
        for x, y, width in best_solution:
            print(f"{x} {y} {width}")


n = int(input())
solve(n)