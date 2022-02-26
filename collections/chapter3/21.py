from math import sqrt


def in_out():
    try:
        x1, y1 = map(int, input('输入圆心坐标：').split())
        r = int(input('输入圆半径：'))
        x2, y2 = map(int, input('输入另一点坐标：').split())
    except (ValueError, SyntaxError):
        print('输入不合法，请重试！')
    else:
        d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return d <= r


if __name__ == '__main__':
    while True:
        print(in_out())
