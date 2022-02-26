# 给出一个整数n，请计算并返回该整数「各位数字之积」与「各位数字之和」的差
def func1(num):
    lst = list(map(int, str(abs(num))))
    g = 1
    for i in lst:
        g *= i
    return g - sum(lst)


# 一个整数列表lst，如果每个数的出现次数都是独一无二的，就返回True；否则返回False
def func2(lst):
    return len(lst) == len(set(lst))


# 给定一个非负整数列表lst，返回lst的排序结果，排序要求首先是奇数在前，偶数在后，
# 然后是按照数字从大到小排序
def func3(lst):
    lst.sort(reverse=True)  # 先从大到小
    return [x for x in lst if x % 2 == 1] + [x for x in lst if x % 2 == 0]


def func3_a(lst):
    # TODO 符合x % 2 == 0条件的数字排在后面
    return sorted(lst, key=lambda x: (x % 2 == 0, -x))


# 给定两个字符串 s 和 t，它们只包含小写字母。字符串 t 由字符串 s 随机重排，然后在
# 随机位置添加一个字母。请找出在 t 中被添加的字母。
def func4(str1, str2):
    if len(str2) - len(str1) == 1:
        for i in str2:
            if i not in str1:
                return i


# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效
def func5(s):
    if len(s) % 2 == 1:
        return False
    lst = []
    d = {')': '(', '}': '{', ']': '['}
    for v in s:
        if v in '([{':
            lst.append(v)
        elif len(lst) > 0:
            tmp = lst.pop()
            if tmp != d.get(v):
                return False
        else:
            return False
    return len(lst) == 0


if __name__ == '__main__':
    # print(func1(456))
    # x = [1, 2, 9, 45]
    # y = [2, 4, 4, 1, 0, 1]
    # print(func2(x), func2(y))
    print(func3_a([6, 3, 2, 4, 5, 1]))
    # print(func4('abcd', 'acdib'))
    # print(func5('()[]{[]}'))
    # print(func5('()[(]{[)]}'))
