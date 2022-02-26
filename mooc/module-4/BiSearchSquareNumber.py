"""
用二分法计算完全平方数的平方根
"""


def biroot(n: int) -> int:
    low, high = 1, n
    while low <= high:
        mid = (low + high) // 2
        if mid ** 2 == n:
            return mid
        elif mid ** 2 < n:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == '__main__':
    print(biroot(18))
