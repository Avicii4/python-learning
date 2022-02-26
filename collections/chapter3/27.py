def print_table():
    try:
        n = int(input('请输入一个正整数：'))
        if n <= 0:
            raise ValueError
    except (ValueError, SyntaxError):
        print('非法输入')
    else:
        print(' \t', end='')
        for i in range(1, n + 1):
            print(i, end='\t')
        print()
        for i in range(1, n + 1):
            print(i, end='\t')
            for j in range(1, n + 1):
                if j <= i:
                    print(i * j, end='\t')
                else:
                    print()
                    break


if __name__ == '__main__':
    while True:
        print_table()
        print()
