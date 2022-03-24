from collections import Counter

# 一处超时
if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    diff = [abs(n - nums.index(n) - 1) for n in nums]
    cnt = Counter(diff)
    for x in sorted(cnt, reverse=True):
        if cnt[x] > 1:
            print('{} {}'.format(x, cnt[x]))
