"""
测试在 while 条件中使用函数（如len）是否影响效率
"""
from typing import List
import datetime


def func1(nums: List[int]) -> int:
    i = 0
    t1 = datetime.datetime.now()
    while i < len(nums):
        i += 1
    t2 = datetime.datetime.now()
    return (t2 - t1).microseconds


def func2(nums: List[int]) -> int:
    i = 0
    t1 = datetime.datetime.now()
    n = len(nums)
    while i < n:
        i += 1
    t2 = datetime.datetime.now()
    return (t2 - t1).microseconds


if __name__ == '__main__':
    nums = list(range(2**20))
    s1 = s2 = 0
    for i in range(1000):
        f1, f2 = func1(nums), func2(nums)
        if f1 < f2:
            s1 += 1
        elif f1 > f2:
            s2 += 1
    print('{}次func1()快，{}次func2()快'.format(s1, s2))
