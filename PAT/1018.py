if __name__ == '__main__':
    n = int(input())
    records = []
    for i in range(n):
        records.append(input().split())
    vict = tie = lose = 0
    # 分别表示甲乙的锤子、剪刀、布的胜利次数
    dct_1 = {'C': 0, 'J': 0, 'B': 0}
    dct_2 = {'C': 0, 'J': 0, 'B': 0}
    for x, y in records:
        if x == y:
            tie += 1
        elif x == 'C':
            if y == 'J':
                vict += 1
                dct_1['C'] += 1
            else:
                lose += 1
                dct_2['B'] += 1
        elif x == 'J':
            if y == 'C':
                lose += 1
                dct_2['C'] += 1
            else:
                vict += 1
                dct_1['J'] += 1
        elif x == 'B':
            if y == 'C':
                vict += 1
                dct_1['B'] += 1
            else:
                lose += 1
                dct_2['J'] += 1
    print(vict, tie, lose)
    print(lose, tie, vict)
    max_1 = max(dct_1, key=lambda t: (dct_1[t], -ord(t)))
    max_2 = max(dct_2, key=lambda t: (dct_2[t], -ord(t)))
    print(max_1, max_2)
