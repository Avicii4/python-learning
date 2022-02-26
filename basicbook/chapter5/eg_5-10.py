"""
一个元素互不相等的列表lst和其中的一个整数n，
要求以n为枢轴进行一轮快排的分治
"""
from random import sample


def partition(lst, n):
    if n not in lst:
        return '输入错误'
    # for i in range(len(lst)):
    #     if lst[i] == n:
    #         break
    low = 0
    high = len(lst) - 1
    while low < high:
        while low < high and lst[high] > n:
            high -= 1
        lst[low] = lst[high]
        while low < high and lst[low] < n:
            low += 1
        lst[high] = lst[low]
    lst[low] = n
    return lst


if __name__ == '__main__':
    arr = sample(range(20), 10)
    print(arr, arr[0])
    print(partition(arr, arr[0]))
