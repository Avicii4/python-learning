"""
计算n以内所有奇数和
"""


def cal_1(n):
    index = n if n % 2 == 0 else n + 1
    return sum(range(1, index, 2))


def cal_2(n):
    res = 0
    i = 1
    while i <= n:
        res += i
        i += 2
    return res


if __name__ == '__main__':
    num = 5
    print(cal_1(num), cal_2(num))
