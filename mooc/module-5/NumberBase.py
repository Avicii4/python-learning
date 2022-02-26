# 实现十进制转二进制
def my_bin(n: int):
    res = []
    v = 1
    if n < 0:
        res.append('-')
        n = -n
    res.append('0b')
    while v <= n // 2:
        # 找到大于 n//2的最小砝码
        v *= 2
    while v > 0:
        # 判断要不要添加该砝码
        if n < v:
            res.append('0')
        else:
            res.append('1')
            n -= v
        v //= 2
    return ''.join(res)


# 将十进制整数n转换成十六进制数
def my_hex(n: int) -> str:
    res = list()
    base = list('0123456789ABCDEF')
    absn = abs(n)
    if absn == 0:
        return '0'
    while absn > 0:
        res.append(base[absn % 16])
        absn //= 16
    if n < 0:
        res.append('-')
    return ''.join(reversed(res))


# 十六进制转二进制
def hex2bin(n: str) -> str:
    return my_bin(int(n, 16))


if __name__ == '__main__':
    while True:
        x = input('输入十六进制：')
        print(hex2bin(x))
