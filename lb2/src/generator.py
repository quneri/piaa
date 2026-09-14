import random


def generate_matrix(n, symmetric=False, min_weight=1, max_weight=100):
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = -1
            elif not symmetric:
                matrix[i][j] = random.randint(min_weight, max_weight)
            elif i < j:
                value = random.randint(min_weight, max_weight)

                matrix[i][j] = value
                matrix[j][i] = value

    return matrix


def save_matrix(matrix, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(str(len(matrix)) + "\n")
        for row in matrix:
            file.write(" ".join(map(str,row)) + "\n")


if __name__ == "__main__":
    n = int(input("Количество вершин: "))
    symmetric = input("Симметричная матрица? (y/n): ").lower() == "y"

    matrix = generate_matrix(n, symmetric)

    save_matrix(matrix, "matrix.txt")

    print("Матрица сохранена в matrix.txt")
