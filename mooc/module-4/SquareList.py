"""
非递减顺序数组A，返回每个数字的平方组成的新数组，也按非递减顺序排序
"""


def square(num_list: list) -> list:
    return sorted(list(map(lambda x: x ** 2, num_list)))


if __name__ == '__main__':
    arr = [-4, 1, 2, 2]
    print(square(arr))
