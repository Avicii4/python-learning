"""
实现PM2.5空气质量问题提醒程序，接收用户输入的PM2.5值，合法的值为0-500之间的整数，
如果PM2.5小于35，打印“空气质量优，建议户外运动”；
如果PM2.5的值在35到75之间（包括35），打印“空气质量良好，建议适度户外运动”；
如果PM2.5的值大于75（包括75），打印“空气污染，请小心！”
利用 异常处理 用户输入不合法的情况，当用户输入不合法时（输入非整数、输入0-500之外的数值）让用户重新输入。
"""


class IllegalInteger(BaseException):
    """
    自定义异常类 接收一个PM值
    """

    def __init__(self, num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num = num


def air_quality():
    try:
        n = eval(input('请输入PM2.5的值：'))
        if not isinstance(n, int):
            raise ValueError
        if n < 0 or n > 500:
            raise IllegalInteger(n)
        if n < 35:
            print("空气质量优，建议户外运动")
        elif n < 75:
            print("空气质量良好，建议适度户外运动")
        else:
            print("空气污染，请小心！")

    except (ValueError, SyntaxError):
        print('输入不合法')
    except IllegalInteger as i:
        print('输入数值{}在0~500之外'.format(i.num))


if __name__ == '__main__':
    while True:
        air_quality()
