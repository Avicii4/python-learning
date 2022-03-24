if __name__ == '__main__':
    n = int(input())
    res = []
    for _ in range(n):
        s = input().split()
        for ch in s:
            if ch[-1] == 'T':
                res.append(ord(ch[0]) - 64)
    print(''.join(map(str, res)), end='')
