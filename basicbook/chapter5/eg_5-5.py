"""
函数接收参数t，返回斐波那契数列中恰好大于t的第一个数
"""


def large_fib(t):
    m = 1
    n = 1
    while m <= t:
        m, n = m + n, m
    return m


if __name__ == '__main__':
    print(large_fib(45))
