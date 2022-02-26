"""
根据邮件的重量和用户是否选择加急计算邮费。
计算规则：重量在1000克以内(包括1000克), 基本费8元。
超过1000克的部分，每500克加收超重费4元，不足500克部分按500克计算；
如果用户选择加急，多收5元。

输入：重量一定是整数，是否加急是一个字符，如果是大写或者小写Y表示加急，否则是不加急。
"""


def fee(weight, is_urgent):
    if weight <= 0:
        return '重量必须大于0'
    if weight <= 1000:
        res = 8
    else:
        res = 8 + ((weight - 1000) // 500) * 4
        if (weight - 1000) % 500 != 0:
            res += 4
    return res + 5 if is_urgent else res


if __name__ == '__main__':
    while True:
        try:
            w = int(input('请输入重量（克）：'))
            u = input('请输入是否加急（Y/N）：')
            if u != 'Y' and u != 'y' and u != 'N' and u != 'n':
                raise ValueError
        except ValueError:
            print('输入有误')
        else:
            urgent = True if u == 'Y' or u == 'y' else False
            print('总计邮费{}元'.format(fee(w, urgent)))
