if __name__ == '__main__':
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(map(int, input().split()))
    for i in range(n):
        a, b, c = nums[i]
        res = 'true' if a + b > c else 'false'
        print('Case #{}: {}'.format(i + 1, res))
