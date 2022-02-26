"""
编写函数判断素数
"""
from math import sqrt


def is_prime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    while True:
        x = eval(input("请输入一个整数："))
        print(is_prime(x))
