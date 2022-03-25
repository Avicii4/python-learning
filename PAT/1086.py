# 注意形如'100'的反转
if __name__ == '__main__':
    a, b = map(int, input().split())
    s = str(a * b)
    print(int(s[::-1]))
