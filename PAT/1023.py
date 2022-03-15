if __name__ == '__main__':
    nums = list(map(int, input().split()))
    res = []
    # 先找出第一个非0作为首位
    for i in range(1, len(nums)):
        if nums[i] != 0:
            res.append(i)
            nums[i] -= 1
            break
    for i in range(len(nums)):
        while nums[i] > 0:
            res.append(i)
            nums[i] -= 1
    if not res:
        res = [0]
    print(''.join(map(str, res)))
