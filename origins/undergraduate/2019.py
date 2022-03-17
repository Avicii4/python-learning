import re
from typing import List
from typing import Tuple
from collections import Counter


def func_1(x: int, y: int) -> int:
    if (x == 1 or x == -1) and -1 <= y <= 1:
        return 0
    elif (y == 1 or y == -1) and -1 <= x <= 1:
        return 0
    elif -1 < x < 1 and -1 < y < 1:
        return 1
    else:
        return -1


def func_2(d: int, l: int, r: int) -> int:
    if 0 <= d <= 9 and l < r:
        return str(''.join(map(str, range(l, r + 1)))).count(str(d))


def func_3(arr: List[int]) -> List[int]:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if not n % i:
                return False
        return True

    arr = list(map(str, arr))
    lst = []
    for x in arr:
        lst.append(int(x[0]))
        lst.append(int(x[-1]))
    res, tmp = [], ''
    for n in lst:
        if is_prime(n):
            if tmp:
                res.append(int(tmp))
            res.append(n)
            tmp = ''
        else:
            tmp += str(n)
    if tmp:
        res.append(int(tmp))
    return res


def func_4(mat: List[List[int]]) -> List[List[int]]:
    m = len(mat)
    # res = [[0 for _ in range(m)] for _ in range(2 * m - 1)]
    nums = []

    # 第一段
    for k in range(m):
        tmp, i, j = [], k, 0
        while i >= 0 and j < m:
            tmp.append(mat[i][j])
            i -= 1
            j += 1
        else:
            nums.append(tmp)
    # 第二段
    for k in range(1, m):
        tmp, i, j = [], m - 1, k
        while i >= 0 and j < m:
            tmp.append(mat[i][j])
            i -= 1
            j += 1
        else:
            nums.append(tmp)
    for i in range(len(nums)):
        while len(nums[i]) != m:
            nums[i].append(0)
    return nums


def func_5(word: str) -> str:
    if len(word) > 1:
        if word.lower() != word:
            return word.capitalize()
        else:
            return word[0].upper() + word[1:-1].lower() + word[-1].upper()


def func_6(s: str) -> str:
    words = re.split(r'[^\da-zA-Z]+', s)
    print(words)
    for i in range(len(words)):
        n = len(words[i])
        if n > 5:
            words[i] = words[i][0] + '*' * (n - 2) + words[i][-1]
    return ' '.join(words)


def func_7(words: List[str], chars: str) -> int:
    res = 0
    c = Counter(chars)
    for word in words:
        if not Counter(word) - c:
            res += 1
    return res


def func_8(lst: List[Tuple]) -> Tuple:
    dct = dict()
    for record in lst:
        if bool(re.search(r'\d{3}', record[0])) \
                and isinstance(record[1], int) and 1 <= record[1] <= 3:
            dct[record[0]] = dct.get(record[0], 0) + record[1]
    if dct:
        x = sorted(dct, key=lambda k: (dct[k], -int(k))).pop()
        return tuple([x, dct[x]])


if __name__ == '__main__':
    # print(func_1(-1, -1))
    # print(func_2(1, 70, 11))
    # print(func_3([123]))
    # print(func_4([[1, 2], [3, 4]]))
    # print(func_5('universe'))
    # print(func_6('hello,.world!54;computer[[5w'))
    # print(func_7(['hello', 'world', 'soochow', 'honey'], 'welldonehoneyr'))
    no = ['471', '120', '006']
    hr = [3, 3, 3]
    print(func_8(list(zip(no, hr))))
