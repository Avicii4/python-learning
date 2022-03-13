from math import pi
from math import ceil

if __name__ == '__main__':
    h, r = map(int, input('请输入半径和高度：').split())
    v = h * pi * r ** 2
    print('需要{}桶水'.format(ceil(20000 / v)))
