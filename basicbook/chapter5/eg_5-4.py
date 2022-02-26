"""
函数接收包含20个整数的列表lst和一个整数k，
将列表下标至在k之前和之后的元素逆序，再整体逆序后输出lst
"""


def rev(lst, k):
    if not isinstance(lst, list) or not isinstance(k, int):
        return '输入类型错误'
    if k < 0 or k > 20 or len(lst) != 20:
        return '输入数据错误'
    lst[:k + 1] = lst[k::-1]
    lst[k + 1:] = lst[len(lst) - 1:k:-1]
    lst[::] = lst[::-1]
    return lst


if __name__ == '__main__':
    arr = list(range(1, 21))
    print(arr)
    print(rev(arr, 4))
