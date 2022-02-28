from typing import List


class Solution:
    # 使用原生排序函数
    def move_zeroes_1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=lambda x: x == 0)

    # 此法时间复杂度极高，不推荐
    def move_zeroes_2(self, nums: List[int]) -> None:
        for n in nums:
            if n == 0:
                nums.remove(n)
                nums.append(0)

    """
    双指针法，算法始终维护一个连续的“0域”，left是其左边界，
    right每次向后，要么吸纳一个新的0，要么将非0数字换到“0域”左侧去
    """
    def move_zeroes_3(self, nums: List[int]) -> None:
        left = right = 0
        n = len(nums)
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


if __name__ == '__main__':
    sol = Solution()
    arr = [1, 0, 2, 0, 0, 3, 9]
    sol.move_zeroes_3(arr)
    print(arr)
