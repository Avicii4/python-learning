"""
函数接收包含若干整数的列表lst，
返回一个元组，第一个元素为lst最小值，其余元素为最小值在lst的下标
"""


def check(lst):
    m = min(lst)
    result = [i for i in range(len(lst)) if lst[i] == m]
    return (m,) + tuple(result)


if __name__ == '__main__':
    l = [1, 2, 3, 5, 1, 1, 35, 1]
    print(check(l))
