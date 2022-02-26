def letter():
    s = input('请输入一个字符：')
    if len(s) == 1:
        if 'A' <= s <= 'Z':
            print(s.lower())
        elif 'a' <= s <= 'z':
            print(s.upper())
        else:
            print(s)
    else:
        print('输入非法')


if __name__ == '__main__':
    while True:
        letter()
