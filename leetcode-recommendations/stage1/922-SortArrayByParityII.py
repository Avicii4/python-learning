from typing import List


class Solution:
    def sort_array_by_parity_II_1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p, q = 0, 1
        while q < n:
            if nums[p] % 2 and nums[q] % 2 == 0:
                nums[p], nums[q] = nums[q], nums[p]
            elif nums[p] % 2 == 0 and nums[q] % 2 == 0:
                t = q + 2
                while not nums[t] % 2:
                    t += 2
                nums[q], nums[t] = nums[t], nums[q]
            elif nums[p] % 2 and nums[q] % 2:
                t = q + 1
                while nums[t] % 2:
                    t += 2
                nums[p], nums[t] = nums[t], nums[p]
            p, q = q + 1, q + 2
        return nums

    # 简化方法，只要确定j所在的是否是奇数就可以
    def sort_array_by_parity_II_2(self, nums: List[int]) -> List[int]:
        n, j = len(nums), 1
        for i in range(0, n, 2):
            if nums[i] % 2 == 1:
                while nums[j] % 2:
                    j += 2
                nums[i], nums[j] = nums[j], nums[i]
        return nums


if __name__ == '__main__':
    sol = Solution()
    nums = [3, 1, 4, 2]
    print(sol.sort_array_by_parity_II_2(nums))
