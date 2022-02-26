"""
猜数字游戏
"""
from random import randint


def guess():
    x = randint(1, 10001)
    counter = 0
    print('已生成数字x！')
    while True:
        try:
            num = int(input('请输入你的猜测：'))
        except ValueError:
            print('输入不合法')
            continue
        else:
            counter += 1
            if num == x:
                print('猜对啦！这个数字就是{}! 你共猜了{}次'.format(x, counter))
                return
            elif num > x:
                print('高了')
            else:
                print('低了')


if __name__ == '__main__':
    while True:
        guess()
