# 一处超时
if __name__ == '__main__':
    m, n, a, b, target = map(int, input().split())
    lst = []
    for _ in range(m):
        lst.append(list(map(int, input().split())))
    for i in range(m):
        for j in range(n):
            if a <= lst[i][j] <= b:
                lst[i][j] = target
            print('{:0>3}'.format(lst[i][j]), end='')
            if j == n - 1:
                print()
            else:
                print(' ', end='')
