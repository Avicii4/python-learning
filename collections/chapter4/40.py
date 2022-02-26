import datetime


def fibo(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)


def loop_fibo(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    while n > 2:
        a, b = b, a + b
        n -= 1
    return b


if __name__ == '__main__':
    while True:
        index = int(input('要求第几项：'))
        if index == 0:
            exit('用户中止')

        if index <= 32:
            t1 = datetime.datetime.now()
            x = fibo(index)
            t2 = datetime.datetime.now()
            print('结果为：{}，递归函数耗时:{}'.format(x, (t2 - t1).microseconds))
        else:
            print('项数过多，递归函数耗时巨大')

        if index <= 500000:
            t1 = datetime.datetime.now()
            x = loop_fibo(index)
            t2 = datetime.datetime.now()
            print('结果为：{}，迭代函数耗时:{}'.format(x, (t2 - t1).microseconds))
        else:
            print('项数过多，迭代函数耗时巨大')
