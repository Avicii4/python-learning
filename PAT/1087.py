if __name__ == '__main__':
    n = int(input())
    res = set()
    for i in range(1, n + 1):
        res.add(i // 2 + i // 3 + i // 5)
    print(len(res))
