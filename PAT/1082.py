if __name__ == '__main__':
    n, res = int(input()), []
    for _ in range(n):
        arr = input().split()
        x, y = map(int, arr[1:])
        res.append((arr[0], x ** 2 + y ** 2))
    res.sort(key=lambda k: k[1])
    print(res[0][0], res[-1][0])
