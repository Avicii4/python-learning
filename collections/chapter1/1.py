if __name__ == '__main__':
    a, b = map(int, input('输入两个整数：').split())
    print('{},{}'.format(a // b, a % b))
