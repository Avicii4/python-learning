from math import sqrt


def output_prime():
    try:
        num = int(input('请输入一个大于2的整数：'))
        if num <= 2:
            raise ValueError
    except (ValueError, SyntaxError):
        print('非法输入')
    else:
        lst = [n for n in range(2, num) if 0 not in [n % i for i in range(2, int(sqrt(n) + 1))]]
        print(lst)


if __name__ == '__main__':
    while True:
        output_prime()
