"""
输入n的值，求
1/1 - 1/2 + 1/3 - 1/4 + 1/5 - 1/6 + 1/7 - 1/8 + ... + (-1)^(n-1)·1/n 的值。
输入一个正整数n。1 <= n <= 1000。
返回一个字符串，该字符串的内容是一个保留小数点后四位整数的浮点数
"""


def calc(n: int) -> str:
    if n < 1 or n > 1000:
        return 'n的范围应是[1,1000]'
    res = 0
    for i in range(1, n + 1):
        res += (1 / i) * (-1) ** (i + 1)    # TODO 乘方优先级高于乘法
    return str('%.4f' % res)


if __name__ == '__main__':
    while True:
        try:
            x = int(input('请输入n：'))
        except ValueError:
            print('n输入不合法')
        else:
            print(calc(x))
