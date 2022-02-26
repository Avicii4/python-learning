def counter(s: str, index: int) -> int:
    s = s.lower()
    return s[index:].count(s[index])


if __name__ == '__main__':
    while True:
        s = input('请输入句子：')
        n = int(input('请输入欲统计的位置：'))
        print(counter(s, n))
