if __name__ == '__main__':
    a, b = input().split('E')
    flag_a, num_a = a[0], a[1] + a[3:]
    b, res = int(b), []
    # 负指数
    if b < 0:
        res = list(('0' * (abs(b)) + num_a))
        res.insert(1, '.')

    if b > 0:
        # 结果里依然有小数点
        if (len(num_a) - 1) > b:
            res = list(num_a)
            res.insert(b + 1, '.')
        # 无小数点
        else:
            res = num_a + ('0' * (b - len(num_a) + 1))

    if b == 0:
        res = a[1:]
    if flag_a == '-':
        print(flag_a, end='')
    print(''.join(res))
