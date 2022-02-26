from math import sqrt


def trangle():
    try:
        x1, y1 = map(float, input('请输入第一个点的坐标：').split())
        x2, y2 = map(float, input('请输入第二个点的坐标：').split())
        x3, y3 = map(float, input('请输入第三个点的坐标：').split())
    except (ValueError, SyntaxError):
        print('输入不合法！')
    else:
        a = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        b = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
        c = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        circumference = a + b + c
        s = circumference / 2
        area = sqrt(s * (s - a) * (s - b) * (s - c))
        if area == 0:
            print('三点共线，无法组成三角形！')
        else:
            print('周长：{}，面积：{}'.format(circumference, area))


if __name__ == '__main__':
    while True:
        trangle()
