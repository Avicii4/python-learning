if __name__ == '__main__':
    nums = input().split()[1:]
    n_set = set()
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            n_set.add(nums[i] + nums[j])
            n_set.add(nums[j] + nums[i])
    print(eval('+'.join(n_set)))
