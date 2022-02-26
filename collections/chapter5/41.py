def modify():
    s = input('请输入字符串：')
    if s == '':
        exit(-1)
    if len(s) < 2:
        print('长度必须大等于2')
    else:
        res = s[:2] + s[-2:]
        print(res)


if __name__ == '__main__':
    while True:
        modify()
