from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        table = dict()
        for i, n in enumerate(nums):
            if target - n in table:
                return [i, table[target - n]]
            table[n] = i
        return []


if __name__ == '__main__':
    sol = Solution()
    ns, t = [2, 7, 11, 15], 18
    print(sol.two_sum(ns, t))
