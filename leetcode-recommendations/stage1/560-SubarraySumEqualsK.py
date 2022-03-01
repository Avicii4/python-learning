from typing import List


class Solution:
    # 暴力法，超时
    def subarray_sum_1(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            cur = 0
            for j in range(i, len(nums)):
                cur += nums[j]
                if cur == k:
                    res += 1
        return res

    # 前缀和暴力搜，也超时
    def subarray_sum_2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        res = 0
        for i in range(n):
            for j in range(i, n):
                if pre[j + 1] - pre[i] == k:
                    res += 1
        return res

    # 前缀和+字典储存出现频次
    def subarray_sum_3(self, nums: List[int], k: int) -> int:
        # 预设一对(0,1)，否则任何以[0]开始的和为k的连续子数组都会被忽略掉
        # 即，如果pre[i]==k, 则子数组[0...i]是一个解
        # 但 pre[i]-k==0, 可0在dct中找不到，则算法就把这种情况扔掉了
        dct = {0: 1}
        res = pre_sum = 0
        n = len(nums)
        for i in range(n):
            pre_sum += nums[i]
            if pre_sum - k in dct:
                res += dct[pre_sum - k]
            dct[pre_sum] = dct.get(pre_sum, 0) + 1
        return res


if __name__ == '__main__':
    sol = Solution()
    while True:
        lst = list(map(int, input('请输入数组：').split()))
        target = int(input('目标和：'))
        print(sol.subarray_sum_3(lst, target))
