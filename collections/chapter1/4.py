from math import sqrt

if __name__ == '__main__':
    while True:
        try:
            x1, y1, x2, y2 = map(int, input('请输入两点坐标（x1,y1,x2,y2）：').split())
            d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            print('两点间距离：{}'.format(d))
        except:
            exit(0)
