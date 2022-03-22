if __name__ == '__main__':
    n, k = map(int, input().split())
    data = []
    for _ in range(n):
        d = input().split()
        data.append((d[0], int(d[1])))
    data.sort(key=lambda x: (-x[1], x[0]), reverse=True)
    last = n // k + n % k
    tmp = []
    for i in range(last):
        d = data.pop()
        if not i % 2:
            tmp.append(d[0])
        else:
            tmp.insert(0, d[0])
    print(' '.join(tmp))
    for _ in range(1, k):
        tmp = []
        for i in range(n // k):
            d = data.pop()
            if not i % 2:
                tmp.append(d[0])
            else:
                tmp.insert(0, d[0])
        else:
            print(' '.join(tmp))
