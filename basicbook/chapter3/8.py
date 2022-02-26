"""
输出由1，2，3，4组成的所有素数，且每个数字最多使用一次
"""
from math import sqrt
from itertools import permutations


def is_prime(n):
    for index in range(2, int(sqrt(n)) + 1):
        if n % index == 0:
            return False
    return True


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    arr = permutations(nums, 4)
    for seq in arr:
        num = int(''.join(map(str, seq)))  # arr里存着一个个tuple，把它们连成一个str
        if is_prime(num):
            print(num, end=' ')
