def calc(s):
    dct = dict()
    for ch in s:
        dct[ch] = dct.get(ch, 0) + 1
    dct_str = str(dct)
    return dct_str[1:-1]


if __name__ == '__main__':
    while True:
        r = input('请输入一个字符串：')
        if r == '':
            exit(-1)
        print(calc(r))
