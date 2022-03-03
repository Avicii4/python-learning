"""
在被除数都是偶数的前提下，/ 2 和// 2 的效率比较
"""
import datetime


# / 比较快
def func1(n):
    t1 = datetime.datetime.now()
    x = []
    for i in range(n):
        x.append(i * (i + 1) / 2)
    t2 = datetime.datetime.now()
    return (t2 - t1).microseconds


def func2(n):
    t1 = datetime.datetime.now()
    x = []
    for i in range(n):
        x.append(i * (i + 1) // 2)
    t2 = datetime.datetime.now()
    return (t2 - t1).microseconds


if __name__ == '__main__':
    m = 2 ** 16
    f1 = f2 = 0
    for i in range(100):
        a = func1(m)
        b = func2(m)
        if a < b:
            f1 += 1
        if a > b:
            f2 += 1
    print('func1()较快：{}'.format(f1))
    print('func2()较快：{}'.format(f2))
