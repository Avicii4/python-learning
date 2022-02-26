"""
自除数 是指可以被它包含的每一位数除尽的数。
例如，128 是一个自除数，
因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
还有，自除数不允许包含 0 。

给定上边界和下边界数字，输出一个列表，
列表的元素是边界（含边界）内所有的自除数。

示例：
输入：

上边界left = 1, 下边界right = 22

输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""


def is_divisible(num: int) -> bool:
    s = str(num)
    if '0' in s:
        return False
    for ch in s:
        if num % int(ch) != 0:
            return False
    return True


if __name__ == '__main__':
    while True:
        left = int(input('上边界：'))
        right = int(input('下边界：'))
        res = [i for i in list(range(left, right + 1)) if is_divisible(i)]
        print(res)
