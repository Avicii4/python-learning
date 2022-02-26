"""
X年X月X日是星期几
"""
import datetime

if __name__ == '__main__':
    arr = ['一', '二', '三', '四', '五', '六', '日']
    # TODO strftime()输出0~6
    day = int(datetime.datetime(2012, 1, 22).strftime('%w'))
    print('星期' + arr[day])
