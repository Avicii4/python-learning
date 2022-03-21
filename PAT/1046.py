if __name__ == '__main__':
    n, record = int(input()), []
    for _ in range(n):
        record.append(list(map(int, input().split())))
    a = b = 0
    for lst in record:
        x = lst[0] + lst[2]
        if x == lst[1] and x != lst[3]:
            b += 1
        elif x == lst[3] and x != lst[1]:
            a += 1
    print(a, b)
