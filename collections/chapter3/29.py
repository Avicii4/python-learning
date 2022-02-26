def sum_nums():
    try:
        n = int(input('Please input the number of numbers:'))
        if n < 0:
            raise ValueError
        if n == 0:
            return
    except (ValueError, SyntaxError):
        print('Invalid input.')
    else:
        lst = [0] * n  # 初始化数组
        try:
            for i in range(n):
                lst[i] = int(input('Please input number {}:'.format(i + 1)))
        except (ValueError, SyntaxError):
            print('Invalid input.')
        else:
            print('sum = {}'.format(sum(lst)))


if __name__ == '__main__':
    while True:
        sum_nums()
