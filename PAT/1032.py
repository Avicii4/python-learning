# 有超时
if __name__ == '__main__':
    n = int(input())
    dct = dict()
    for _ in range(n):
        info = input().split()
        dct[info[0]] = dct.get(info[0], 0) + int(info[1])
    x = sorted(dct, key=lambda k: dct[k]).pop()
    print(x, dct[x])
