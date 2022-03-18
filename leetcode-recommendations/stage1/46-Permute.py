from typing import List
from itertools import permutations


class Solution:
    def permute_1(self, nums: List[int]) -> List[List[int]]:
        p = permutations(nums, len(nums))
        m = map(list, list(p))
        return list(m)

    # python itertools 的具体实现，需要组合数学的知识，很难理解
    def permute_2(self, nums: List[int]) -> List[List[int]]:
        res = []
        pool = tuple(nums)
        n = len(pool)

        indices = list(range(n))
        cycles = list(range(n, 0, -1))
        res.append([pool[i] for i in indices[:n]])
        while n:
            for i in reversed(range(n)):
                cycles[i] -= 1
                if cycles[i] == 0:
                    indices[i:] = indices[i + 1:] + indices[i:i + 1]
                    cycles[i] = n - i
                else:
                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    res.append([pool[i] for i in indices[:n]])
                    break
            else:
                return res

    # 递归
    def permute_3(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:  # 递归边界条件
            return [nums]
        else:
            res = []
            for i in range(len(nums)):
                rest = nums[:i] + nums[i + 1:]  # 除[i]之外的元素
                for x in self.permute_3(rest):
                    res.append(nums[i:i + 1] + x)  # 把[i]放在首位
            return res

    # 回溯法
    def permute_4(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtrace(cur=0):
            # 终止条件
            if cur == n and nums[:] not in res:
                res.append(nums[:])
            for i in range(cur, n):
                # 尝试交换目前值与cur之后的每个值
                nums[cur], nums[i] = nums[i], nums[cur]
                # 递归进入下个位置
                backtrace(cur + 1)
                # 恢复现场
                nums[cur], nums[i] = nums[i], nums[cur]

        backtrace()
        return res


if __name__ == '__main__':
    sol = Solution()
    # nums = [1, 2, 3]
    # print(sol.permute_1(nums))
    arr = [5, 6, 6, 9]
    res = sol.permute_4(arr)
    for r in res:
        print(r)
