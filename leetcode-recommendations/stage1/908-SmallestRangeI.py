from typing import List


class Solution:
    def smallest_range(self, nums: List[int], k: int) -> int:
        # return max(0, max(nums) - min(nums) - 2 * k)
        res = max(nums) - min(nums) - 2 * k
        return res if res >= 0 else 0


if __name__ == '__main__':
    sol = Solution()
    arr = [1, 3, 6]
    print(sol.smallest_range(arr, 3))
