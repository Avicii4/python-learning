"""
实现二分查找
"""


def bisearch(L, t, low, high):
    while low <= high:
        mid = (low + high) // 2
        if L[mid] == t:
            return True
        elif L[mid] > t:
            high = mid - 1
        else:
            low = mid + 1
    return False


if __name__ == '__main__':
    L = [1, 4, 9, 15, 16, 21, 33, 185, 984]
    print(bisearch(L, 185, 0, len(L) - 1))
