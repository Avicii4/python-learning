def calc():
    try:
        x = int(input('输入一个三位数:'))
        if not 100 <= x <= 999:
            raise ValueError
        res = sum(map(int, str(x)))
        print(str(res).rjust(4))
    except (ValueError, SyntaxError):
        print('输入不合法')


if __name__ == '__main__':
    while True:
        calc()
