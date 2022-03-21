x = ['tret', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jly', 'aug', 'sep', 'oct', 'nov', 'dec']
y = ['', 'tam', 'hel', 'maa', 'huh', 'tou', 'kes', 'hei', 'elo', 'syy', 'lok', 'mer', 'jou']


def earth_to_mars(num: int):
    p, q = num // 13, num % 13
    if not p:
        print(x[q])
    else:
        if q == 0:
            # 个位的零不用输出
            print(y[p])
        else:
            print(y[p], x[q])


def mars_to_earth(s: str):
    lst = s.split()
    if len(lst) == 1:
        if lst[0] in x:
            print(x.index(lst[0]))
        else:
            print(y.index(lst[0]) * 13)
    else:
        p, q = lst
        print(y.index(p) * 13 + x.index(q))


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input()
        if s.isdigit():
            earth_to_mars(int(s))
        else:
            mars_to_earth(s)
