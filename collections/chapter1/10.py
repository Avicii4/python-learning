from random import uniform  # TODO随机浮点数
from math import pi

if __name__ == '__main__':
    r = uniform(5, 20)
    v = 4 / 3 * pi * r ** 3
    print('{:.3f}'.format(r).rjust(15))
    print('{:.3f}'.format(v).rjust(15))
