from math import sqrt


def solve(a, b, c):
    if a == 0:
        print('a不能为0！')
        return
    delta = b ** 2 - 4 * a * c
    if delta == 0:  # 两重根
        x = -b / (2 * a)
        print('x1 = x2 ={:.5f}'.format(x))
    elif delta > 0:  # 两实根
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        print('x1 ={:.5f},x2 ={:.5f}'.format(x1, x2))
    else:  # 复数根
        m = abs(-b / (2 * a))
        n = abs(sqrt(-delta) / (2 * a))
        print('x1 ={0:.5f}+{1:.5f}i, x2 ={0:.5f}-{1:.5f}i'.format(m, n))


if __name__ == '__main__':
    solve(45, 32, 90)
