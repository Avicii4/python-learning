if __name__ == '__main__':
    """
    1. 前17位是否全为数字
    2. 最后1位校验码计算准确
    """
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(input())
    weight = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    z_lst = list(range(11))
    m_lst = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    err_lst = []
    for num in nums:
        s = 0
        for i in range(17):
            if not '0' <= num[i] <= '9':
                err_lst.append(num)
                break
            else:
                s += int(num[i]) * weight[i]
        else:
            if m_lst[s % 11] != num[-1]:
                err_lst.append(num)
    if not err_lst:
        print('All passed')
    else:
        for x in err_lst:
            print(x)
