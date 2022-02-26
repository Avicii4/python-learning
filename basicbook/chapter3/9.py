"""
分段函数计算
"""


def function(x):
    if x < 0:
        return 0
    elif x < 5:
        return x
    elif x < 10:
        return 3 * x - 5
    elif x < 20:
        return 0.5 * x - 2
    else:
        return 0


if __name__ == '__main__':
    while True:
        x = eval(input("x = "))
        print(function(x))
