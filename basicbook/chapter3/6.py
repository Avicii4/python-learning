"""
用户输入小于1000的整数，对其进行因式分解
"""


def dissolve(num):
    result = []
    temp = num
    for i in range(2, num + 1):
        while temp != 0:
            if temp == 1:     # 这句漏写，temp为素数时，while进入死循环
                break
            elif temp % i == 0:
                result.append(i)
                temp /= i
            else:
                i += 1
    print('{0} = '.format(num), ' x '.join(map(str, result)))


if __name__ == '__main__':
    while True:
        n = eval(input('请输入小于1000的整数：'))
        if isinstance(n, int) and n < 1000:
            dissolve(n)
        else:
            print('输入不合法，重新输入')
