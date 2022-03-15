if __name__ == '__main__':
    kaprekar = 6174
    # 注意输入的不一定是4位数字
    num = list('{:0>4}'.format(input()))
    res = -1
    while res != kaprekar and res != 0:
        a, b = int(''.join(sorted(num, reverse=True))), int(''.join(sorted(num)))
        res = a - b
        print('{:0>4} - {:0>4} = {:0>4}'.format(a, b, res))
        num = list('{:0>4}'.format(res))
