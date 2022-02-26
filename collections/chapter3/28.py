def star_hexagon():
    try:
        n = int(input('请输入一个正整数：'))
        if n <= 0:
            raise ValueError
    except (ValueError, SyntaxError):
        print('非法输入')
    else:
        width = 4 * n - 3
        for i in range(n, 2 * n):
            print(' '.join(list('*' * i)).center(width))
        for i in range(2 * n - 2, n - 1, -1):
            print(' '.join(list('*' * i)).center(width))


if __name__ == '__main__':
    while True:
        star_hexagon()
