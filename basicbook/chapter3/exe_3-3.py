"""
判断某一日是某年第几天
"""
import time


def judge_day(year, month, day):
    day_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        day_month[1] = 29
    if month == 1:
        return day
    else:
        return sum(day_month[:month - 1]) + day


if __name__ == '__main__':
    date = time.localtime()
    # a, b, c = 2019, 12, 10
    a, b, c = date[:3]
    print(judge_day(a, b, c))
