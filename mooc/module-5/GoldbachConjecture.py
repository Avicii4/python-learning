"""
验证哥德巴赫猜想
"""
from math import sqrt
import datetime
import sympy


def is_prime(n: int) -> bool:
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def goldbach(n: int):
    if n < 2:
        return '输入必须大于2'
    if n % 2 != 0:
        return '输入必须为偶数'
    for i in range(2, n - 1):
        if is_prime(i) and is_prime(n - i):
            return '验证成功！{} = {} + {}'.format(n, i, n - i)
    return '哥德巴赫不对'


def fast_goldbach(n: int):
    if n < 2:
        return '输入必须大于2'
    if n % 2 != 0:
        return '输入必须为偶数'
    for i in range(2, n - 1):
        if sympy.isprime(i) and is_prime(n - i):
            return '验证成功！{} = {} + {}'.format(n, i, n - i)
    return '哥德巴赫不对'


if __name__ == '__main__':
    num = 1234567897817104
    t1 = datetime.datetime.now()
    goldbach(num)
    t2 = datetime.datetime.now()
    print('慢速函数耗时：{}'.format((t2-t1).microseconds))

    t1 = datetime.datetime.now()
    fast_goldbach(num)
    t2 = datetime.datetime.now()
    print('快速函数耗时：{}'.format((t2-t1).microseconds))
