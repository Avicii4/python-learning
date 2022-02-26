"""
求一个数的平方根：
start = 0 end = n
判断(start+end)/2的平方与n的大小关系
    差的绝对值小于0.0000001则认为正确
    前者大，end=(start+end)/2
    后者大，start=(start+end)/2
"""


def root(num):
    start, end = 0, num
    tmp = (start + end) / 2
    while abs(tmp ** 2 - num) > 1e-6:    # TODO 注意科学记数法的写法
        tmp = (start + end) / 2
        if tmp ** 2 > num:
            end = (start + end) / 2
        else:
            start = (start + end) / 2
    return tmp


if __name__ == '__main__':
    while True:
        x = int(input('请输入一个整数：'))
        print('{}的平方根为：{}'.format(x, root(x)))
