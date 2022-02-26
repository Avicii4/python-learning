"""
用二分法计算根号二
"""

if __name__ == '__main__':
    index = 1e-10
    low, high = 1, 2
    while low <= high:
        mid = (low + high) / 2
        miss = abs(mid ** 2 - 2)
        if miss <= index:
            print(mid)
            exit()
        elif mid ** 2 > 2:
            high = mid
        else:
            low = mid

