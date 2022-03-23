if __name__ == '__main__':
    n = int(input())
    m = -1
    for _ in range(n):
        a, b = map(int, input().split())
        r = (a ** 2 + b ** 2) ** 0.5
        if r > m:
            m = r
    print('{:.2f}'.format(m))
