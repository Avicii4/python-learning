def bank():
    try:
        base = int(input('请输入一个整数：'))
    except (ValueError, SyntaxError):
        print('输入不合法')
    else:
        res = 0
        if base <= 0:
            print('本金必须为正数')
            return
        elif base < 100000:
            res = base * 1.015
        elif base < 500000:
            res = base * 1.02
        elif base < 1000000:
            res = base * 1.03
        else:
            res = base * 1.035
        print('一年后本息合计{:.2f}元'.format(res))


if __name__ == '__main__':
    while True:
        bank()
