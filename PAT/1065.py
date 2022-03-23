# 两处超时
if __name__ == '__main__':
    n, cp = int(input()), []
    for _ in range(n):
        cp.extend(input().split())
    m = int(input())
    guest = input().split()
    res = []
    for g in guest:
        if g not in cp:
            res.append(g)
        else:
            idx = cp.index(g)
            # 偶数号，伴侣是后一个
            if not idx % 2:
                if cp[idx + 1] not in guest:
                    res.append(g)
            # 奇数号，伴侣是前一个
            else:
                if cp[idx - 1] not in guest:
                    res.append(g)
    print(len(res))
    if res:
        print(' '.join(sorted(res)))
