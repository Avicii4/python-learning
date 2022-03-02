from typing import List


class Solution:
    # 纯暴力，超时
    def maximum_product_1(self, nums: List[int]) -> int:
        max = nums[0] * nums[1] * nums[2]
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    p = nums[i] * nums[j] * nums[k]
                    max = p if p > max else max
        return max

    def maximum_product_2(self, nums: List[int]) -> int:
        # 按绝对值倒序排列
        nums.sort(key=lambda x: -abs(x))
        max_p = nums[0] * nums[1] * nums[2]
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    p = nums[i] * nums[j] * nums[k]
                    if p > 0:
                        # 假如乘积是正的，肯定是答案
                        return p
                    max_p = p if p > max_p else max_p
        return max_p

    # 只要找出数组的第一、第二、第三大的值和第一、第二小的值即可
    def maximum_product_3(self, nums: List[int]) -> int:
        max1 = max2 = max3 = min(nums)
        min1 = min2 = max(nums)
        for num in nums:
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num
            # 这里千万不要写elif
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num
        return max(max1 * max2 * max3, max1 * min1 * min2)


if __name__ == '__main__':
    sol = Solution()
    while True:
        lst = list(map(int, input('请输入数组：').split()))
        if not lst:
            exit(-1)
        print(sol.maximum_product_3(lst))
