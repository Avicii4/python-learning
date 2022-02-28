def detail(points: float, total: int):
    nums = [0] * 6
    try:
        for a0 in range(total + 1):
            for a1 in range(total - a0 + 1):
                for a2 in range(total - a0 - a1 + 1):
                    for a3 in range(total - a0 - a1 - a2 + 1):
                        for a4 in range(total - a0 - a1 - a2 - a3 + 1):
                            a5 = total - a0 - a1 - a2 - a3 - a4
                            cur_points = (a1 * 2 + a2 * 4 + a3 * 6 + a4 * 8 + a5 * 10) / total
                            if abs(cur_points - points) < 1e-3:
                                nums[0], nums[1], nums[2], nums[3], nums[4], nums[5] = a0, a1, a2, a3, a4, a5
                                raise ValueError
    except ValueError:
        for i in range(6):
            print('打{}星的有：{} 人'.format(i, nums[i]))


if __name__ == '__main__':
    while True:
        p = float(input('请输入总评分：'))
        t = int(input('请输入评分人数：'))
        if p == t == 0:
            exit('用户主动中止')
        detail(p, t)
