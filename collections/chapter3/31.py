def sums():
    try:
        a, n = map(int, input('请分别输入a和n的值：').split())
        if n < 0 or not 0 <= a <= 9:
            raise ValueError
    except (ValueError, SyntaxError):
        print('输入非法')
    else:
        if a == 0 or n == 0:
            print(0)
        else:
            lst = [''] * n
            for i in range(n):
                lst[i] = str(a) * (i + 1)
            lst = map(int, lst)
            print(sum(lst))


if __name__ == '__main__':
    while True:
        sums()
