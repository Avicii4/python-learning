"""
奶茶10元一杯，
每买3杯送1杯或每买5杯送2杯；
小强带了N元钱（N>=0）；
请问小强最多可以买多少杯？
"""


def buy_tea(money):
    money //= 10
    n = 7 * (money // 5)  # 优先买五送二
    money %= 5
    n += 4 * (money // 3)  # 再买三送一
    money %= 3
    n += money
    return n


if __name__ == '__main__':
    while True:
        try:
            n = int(input('小强携带金额：'))
        except ValueError:
            print('输入数据不合法')
        else:
            if n < 0:
                print('金额必须大于0')
            else:
                print('最多可买{}杯'.format(buy_tea(n)))
