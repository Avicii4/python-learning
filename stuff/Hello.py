from math import sqrt


# 输出100以内所有素数
def prime_num():
    x = []
    for n in range(2, 100, 1):
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                break
        else:
            x.append(n)


# 乘法表
def multiplication_table():
    for j in range(1, 10):
        for i in range(1, j + 1):
            print('{0}x{1}={2}'.format(i, j, i * j), end='\t')
            if i == j:
                print()


def hh(lst, k):
    if not isinstance(lst, list) or not isinstance(k, int):
        return '输入类型错误'
    if k < 0 or k > 20 or len(lst) != 20:
        return '输入数据错误'
    lst[:k + 1] = lst[k::-1]
    lst[k + 1:] = lst[len(lst) - 1:k:-1]
    lst[::] = lst[::-1]
    return lst


def aa():
    for rabbit in range(0, 36):
        ch = 36 - rabbit
        if 2 * ch + 4 * rabbit == 94:
            print('鸡有{}只，兔有{}只'.format(ch, rabbit))


if __name__ == '__main__':
    #x = int(''.join(list(map(str, list(range(1, 10))))))
    aa()
