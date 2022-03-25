from collections import Counter


def func_1(n):
    arr = []
    for i in range(1, n + 1):
        s = bin(i)[2:]
        m = s.count('1')
        if m > len(s) - m:
            arr.append(i)
    return arr
    # return [x for x in range(1, n + 1) if bin(x)[2:].count('1') > bin(x)[2:].count('0')]


# 不好验证正确性
# def func_2(lst):
#     lst.sort(reverse=True)
#     a = lst[0] * lst[1]
#     b = lst[-1] * lst[-2]
#     return (lst[1], lst[0]) if a >= b else (lst[-1], lst[-2])

def func_2(lst):
    a, b = lst[0:2]
    cur, n = a * b, len(lst)
    for i in range(n - 1):
        for j in range(i + 1, n):
            tmp = lst[i] * lst[j]
            if tmp > cur:
                a, b, cur = lst[i], lst[j], tmp
            elif tmp == cur and a + b < lst[i] + lst[j]:
                a, b = lst[i], lst[j]
    return (a, b) if a >= b else (b, a)


def func_3(nums):
    res, n = [], len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                res.append(nums[j])
                break
        else:
            res.append(None)
    return res + [None]


def func_4(lst):
    n, res = len(lst), set()
    nums = [x for item in lst for x in item]
    cnt = Counter(nums)
    for i in cnt:
        if cnt[i] > n // 2:
            res.add(i)
    return res


if __name__ == '__main__':
    # print(func_1(100))
    # print(func_2([-2, -2, 0]))
    # print(func_3([7, 3, 5]))
    print(func_4([{1, 2}, {1, 2, 3}]))
