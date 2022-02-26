"""
给定一个十进制正整数n，写下从1到n的所有整数，然后数一下其中出现的数字“1”的个数。
例如当n=2时，写下1,2。这样只出现了1个“1”；
当n=12时，写下1，2，3，4，5，6，7，8，9，10，11，12。这样出现了5个“1”。
输入：正整数n。1 <= n <= 10000。
"""


def count(n: int) -> int:
    if n < 1 or n > 10000:
        return -1
    s = ','.join(map(str, range(1, n + 1)))
    print(s)
    return s.count('1')


if __name__ == '__main__':
    while True:
        try:
            x = int(input('请输入正整数n：'))
        except ValueError:
            print('输入错误')
        else:
            res = count(x)
            print('其中共有{}个‘1’'.format(res))
