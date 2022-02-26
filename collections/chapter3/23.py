def output_nums():
    try:
        lst = list(map(int, input('请输入三个整数：').split()))
    except (ValueError, SyntaxError):
        print('输入不合法')
    else:
        if len(lst) != 3:
            print('个数不符合要求')
        else:
            for i in sorted(lst):
                print(i, end=' ')
                print()


if __name__ == '__main__':
    while True:
        output_nums()
