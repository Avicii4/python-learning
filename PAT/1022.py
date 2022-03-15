if __name__ == '__main__':
    a, b, d = map(int, input().split())
    res, num = [], a + b
    while num:
        res.append(num % d)
        num //= d
    if not res:
        res = [0]
    print(''.join(map(str, res[::-1])))
