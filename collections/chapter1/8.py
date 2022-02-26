if __name__ == '__main__':
    # 复利计算
    deposit = 0
    month = 5
    for i in range(month):
        deposit += 100
        deposit += 0.005 * deposit
    print('{}个月后余额{:.5f}'.format(month, deposit))
    base = month * 100
    print('收益率{:.2%}'.format((deposit - base) / base))
