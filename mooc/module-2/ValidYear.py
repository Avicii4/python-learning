"""
从键盘输入年月日，判断是否合法
"""


def is_valid_year(year, month, day):
    if year < 0 or month < 0 or day < 0 or month > 12 or day > 31:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return day <= 31
    elif month in [4, 6, 9, 11]:
        return day <= 30
    else:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  # TODO 闰年是 400的倍数 或者 是4的倍数且不是100的倍数
            return day <= 29
        else:  # 平年
            return day <= 28


if __name__ == '__main__':
    while True:
        try:
            s = input('请输入年月日：')
            y, m, d = [int(x) for x in s.split('-')]
        except ValueError:
            print('年月日输入不合法')
        else:
            print(is_valid_year(y, m, d))
