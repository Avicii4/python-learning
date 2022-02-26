from random import randint

if __name__ == '__main__':
    for i in range(10):
        x = randint(100, 1000)
        print('生成三位数{}，\n逆置后{}'.format(x, int(str(x)[::-1])))
