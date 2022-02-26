def modify():
    try:
        num = eval(input('请输入一个不超过5位的正整数：'))
        if isinstance(num, float):
            print('必须是整数')
            return
        if not isinstance(num, int):
            raise ValueError
    except (ValueError, SyntaxError, NameError):
        print('非法输入')
    else:
        if num <= 0:
            print('必须是正整数')
        elif num > 99999:
            print('不能超过5位')
        else:
            num_str = str(num)
            lst = ['一', '二', '三', '四', '五']
            print('是{}位数'.format(lst[len(num_str) - 1]))
            for c in num_str:
                print(c, end=' ')
            print()
            print(num_str[::-1])


if __name__ == '__main__':
    while True:
        modify()
