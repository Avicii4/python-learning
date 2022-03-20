if __name__ == '__main__':
    n, table = int(input()), []
    for _ in range(n):
        table.append(input().split())
    k = [item[1] for item in table]
    m = int(input())
    try_nums = list(map(int, input().split()))
    res = []
    for x in try_nums:
        arr = table[k.index(str(x))]
        res.append('{} {}'.format(arr[0],arr[2]))
    for i in res:
        print(i)

