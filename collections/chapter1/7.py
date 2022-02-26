from math import sqrt


def triangle():
    x1, y1 = map(int, input('第一个点的坐标：').split())
    x2, y2 = map(int, input('第二个点的坐标：').split())
    x3, y3 = map(int, input('第三个点的坐标：').split())
    side1 = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    side2 = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    side3 = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    s = (side1 + side2 + side3) / 2
    area = sqrt(s * (s - side1) * (s - side2) * (s - side3))
    print('{:.2f}'.format(area).rjust(7))    # 右对齐 占7列 保留2位小数


if __name__ == '__main__':
    triangle()
