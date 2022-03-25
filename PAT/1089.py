def solve():
    n, lst = int(input()), []
    for _ in range(n):
        lst.append(int(input()))
    lst.insert(0, None)
    # 假设 i,j 是狼人
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            wolf_lie = human_lie = 0
            for k in range(1, n + 1):
                # k号说谎
                if (lst[k] < 0 and abs(lst[k]) != i and abs(lst[k]) != j) \
                        or (lst[k] > 0 and (lst[k] == i or lst[k] == j)):
                    # 说谎的狼人
                    if k == i or k == j:
                        wolf_lie += 1
                        if wolf_lie > 1:
                            break
                    # 好人说谎
                    else:
                        human_lie += 1
                        if human_lie > 1:
                            break
            else:
                if wolf_lie == human_lie == 1:
                    print(i, j)
                    return
    print('No Solution')


if __name__ == '__main__':
    solve()
