"""
计算距离某日期X天是什么日期
其中X可为负
"""

import datetime


def process():
    try:
        y, m, d = map(int, input('请输入日期：').split('-'))
        index = int(input('间隔几天：'))
    except ValueError:
        print('输入有误')
    else:
        someday = datetime.datetime(y, m, d)
        if index < 0:
            res = someday - datetime.timedelta(days=-index)
        else:
            res = someday + datetime.timedelta(days=index)
        print(someday.strftime('%Y年%m月%d日') + '间隔{}天是：'.format(index) + res.strftime('%Y年%m月%d日'))


if __name__ == '__main__':
    while True:
        process()
