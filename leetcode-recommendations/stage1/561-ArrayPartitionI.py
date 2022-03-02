from typing import List


class Solution:
    def array_pair_sum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])


if __name__ == '__main__':
    sol = Solution()
    ns = [6, 2, 6, 5, 1, 2]
    print(sol.array_pair_sum(ns))
