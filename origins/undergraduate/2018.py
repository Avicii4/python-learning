from collections import Counter
from typing import List
from typing import Tuple
import re


def func_1(m: int, n: int) -> bool:
    if m > 1 and n > 1:
        return (m % n != 0) and (n % m != 0)


def func_2(lst: List[int]) -> int:
    res, n = 0, len(lst)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if lst[i] > lst[j]:
                res += 1
    return res


def func_3(mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
    m, d, n = len(mat1), len(mat2), len(mat2[0])
    res = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(d):
                res[i][j] += mat1[i][k] * mat2[k][j]
    return res


def func_4(arr: List[int]) -> List[List[int]]:
    res, n = [], int(len(arr) ** 0.5)
    for i in range(n):
        res.append(arr[n * i:n * (i + 1)])
    return res


def func_5(s: str) -> List[str]:
    cnt = Counter(s.split())
    lst = sorted(cnt, key=lambda x: (cnt[x], x), reverse=True)
    return lst[:3]


def func_6(s: str, t: str) -> Tuple[int]:
    s, t = set(s), set(t)
    n = len(t)
    a = b = 0
    for ch in s:
        if ch in t:
            a += 1
            t.remove(ch)
        else:
            b += 1
    return tuple([a, b, n - a])


def func_7(s: str) -> List:
    cnt = Counter(s.upper())
    x = sorted(cnt, key=lambda t: cnt[t]).pop()
    return [x, cnt[x]]


def func_8(s: str) -> List[int]:
    pattern = re.compile(r'\d{3,5}')
    lst = pattern.findall(s)
    lst.sort(key=lambda x: eval('+'.join(x)) / len(x), reverse=True)
    return list(map(int, lst))


if __name__ == '__main__':
    # print(func_1(2, 3))
    # print(func_2([4, 5, 3, 2, 1]))
    # mat1 = [[1, 2], [1, 3]]
    # mat2 = [[1, 1], [1, 0]]
    # print(func_3(mat1, mat2))
    # print(func_4([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    # print(func_5('io io app'))
    # print(func_6('hello','python'))
    # print(func_7('a'))
    print(func_8('12sud456jndf1209uisd898ud99999'))
