"""
穷举法找1-100间的勾股数
"""
from math import sqrt
import datetime


def func_1():
    counter = 0
    for a in range(1, 101):
        for b in range(1, 101):
            for c in range(1, 101):
                if a < b < c and a ** 2 + b ** 2 == c ** 2:
                    print((a, b, c), end='\t')
                    counter += 1
                    if counter == 5:
                        print()
                        counter = 0


def func_2():
    counter = 0
    for a in range(1, 101):
        for b in range(1, 101):
            c = sqrt(a ** 2 + b ** 2)
            if c == int(c) and 0 < c < 101 and a < b < c:
                print((a, b, int(c)), end='\t')
                counter += 1
                if counter == 5:
                    print()
                    counter = 0


if __name__ == '__main__':
    t1 = datetime.datetime.now()
    func_1()
    t2 = datetime.datetime.now()
    print('func_1()用时：{}'.format((t2 - t1).microseconds))
    t1 = datetime.datetime.now()
    func_2()
    t2 = datetime.datetime.now()
    print('func_2()用时：{}'.format((t2 - t1).microseconds))

