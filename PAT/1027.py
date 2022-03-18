# 注意每一行的最后不能有空格，故输出时不能用center()方法
if __name__ == '__main__':
    n, sign = input().split()
    k, n, s = 1, int(n), 1
    while s <= n:
        s += 2 * ((2 * k) + 1)
        k += 1
    k -= 1
    for i in range(k, 0, -1):
        print(' ' * (k - i) + sign * (2 * i - 1))
    for i in range(2, k + 1):
        print(' ' * (k - i) + sign * (2 * i - 1))
    print(n - 2 * sum(range(1, 2 * k, 2)) + 1)
