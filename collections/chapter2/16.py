from random import randint


def print_matrix(m):
    for row in m:
        for elem in row:
            print(elem, end='\t')
        print()


if __name__ == '__main__':
    matrix = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            matrix[i][j] = randint(0, 100)
    print_matrix(matrix)
    for i in range(4):
        for j in range(4):
            if i > j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    print('转置后')
    print_matrix(matrix)
