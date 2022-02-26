# 不考虑输入检查
def matrix_add():
    n = int(input('Please input the number of rows:'))
    m = int(input('Please input the number of columns:'))
    matrix_1 = [[0 for _ in range(m)] for _ in range(n)]  # 二维初始化
    matrix_2 = [[0 for _ in range(m)] for _ in range(n)]
    res = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            matrix_1[i][j] = int(input('Please input A[{},{}]:'.format(i, j)))

    for i in range(n):
        for j in range(m):
            matrix_2[i][j] = int(input('Please input B[{},{}]:'.format(i, j)))

    for i in range(n):
        for j in range(m):
            res[i][j] = matrix_1[i][j] + matrix_2[i][j]
    print(res)


if __name__ == '__main__':
    matrix_add()
