def read_matrix(filename):
    with open(filename, "r", encoding="utf-8") as file:

        lines = file.readlines()

    n = int(lines[0])
    matrix = []

    for i in range(1, n + 1):
        matrix.append(list(map(float, lines[i].split())))

    return matrix
