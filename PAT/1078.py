def compress(s: str) -> str:
    res, cnt = '', 1
    for i in range(len(s)):
        if i == len(s) - 1:
            if cnt > 1:
                res += '{}{}'.format(cnt, s[i])
            else:
                res += s[i]
        elif s[i] == s[i + 1]:
            cnt += 1
        elif cnt > 1:
            res += '{}{}'.format(cnt, s[i])
            cnt = 1
        else:
            res += s[i]
    return res


def decompress(s: str) -> str:
    res, i = '', 0
    while i < len(s):
        if s[i].isdigit():
            j = i + 1
            while s[j].isdigit():
                j += 1
            res += s[j] * int(''.join(s[i:j]))
            i = j + 1
        else:
            res += s[i]
            i += 1
    return res


if __name__ == '__main__':
    r = input()
    s = input()
    if r == 'C':
        print(compress(s))
    else:
        print(decompress(s))
