if __name__ == '__main__':
    n, m = map(int, input().split())
    # 这个是关键
    m %= n
    lst = input().split()
    lst_re = lst[-m:] + lst[:-m]
    print(' '.join(lst_re))
