"""
字符串中包含若干长度小于 15 的十进制或八进制数字，
数字之间用','分开，数字内部存在且仅存在空格。八进
制数以起始位 0 作为标示与十进制数区分。
要求顺序读取这些数字，将它们转变为十进制数后从大到
小排序，输出到 2009.txt
例如输入：235,34_2,043_1_,1_3
分别是十进制 235 ，十进制 342 ，八进制 431 ，
十进制 13 ， _ 代表空格
"""


def convert(s: str):
    nums = s.split(',')
    lst = []
    for n in nums:
        n = ''.join(n.split())
        if n[0] == '0':
            lst.append(str(int(n[1:], 8)))
        else:
            lst.append(n)
    with open('file/2009.txt', 'w', encoding='utf-8') as f:
        for i in lst:
            f.write(i + '\n')


if __name__ == '__main__':
    l = '89 0,07 4 1,120,45 1,064 1'
    convert(l)
