def print_star():
    try:
        n = int(input('请输入行数：'))
        if n <= 0:
            raise ValueError
    except (ValueError, SyntaxError):
        print('非法输入')
    else:
        width = 2 * n - 1
        for i in range(n):
            s = '*' * (2 * i + 1)
            print(s.center(width))


if __name__ == '__main__':
    while True:
        print_star()
