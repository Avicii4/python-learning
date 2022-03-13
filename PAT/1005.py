if __name__ == '__main__':
    k = int(input())
    lst = list(map(int, input().split()))
    lst_copy = lst[:]
    for n in lst_copy:
        while n != 1:
            if n % 2:
                n = (3 * n + 1) // 2
            else:
                n //= 2
            if n in lst:
                lst.remove(n)
    res = list(map(str, sorted(lst, reverse=True)))
    print(' '.join(res))
