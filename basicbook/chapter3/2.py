"""
判断一年是否是闰年
"""


def is_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


if __name__ == '__main__':
    while True:
        x = eval(input("年份输入："))
        if isinstance(x, int):
            print(is_leap_year(x))
        else:
            break
