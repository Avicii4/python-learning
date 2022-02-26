def modify():
    s = input('请输入字符串：')
    if len(s) == 0:
        exit(-1)
    n = int(input('欲删除第几个字符：'))
    if not 1 <= n <= len(s):
        print('范围错误')
        return
    print(s[:n - 1] + s[n:])


if __name__ == '__main__':
    while True:
        modify()
