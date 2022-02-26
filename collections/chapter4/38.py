def reverse(s: str) -> str:
    lst = s.split()
    return ' '.join(lst[::-1])


if __name__ == '__main__':
    while True:
        s = input('请输入句子：')
        if s == '':
            exit(-1)
        print(reverse(s))
