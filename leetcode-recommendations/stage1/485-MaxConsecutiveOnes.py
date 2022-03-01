from typing import List


class Solution:
    def find_max_consecutive_ones(self, nums: List[int]) -> int:
        tmp = cur = 0
        for i in nums:
            if i == 1:
                cur += 1
            else:
                tmp = cur if cur > tmp else tmp
                cur = 0
        return max(tmp, cur)


if __name__ == '__main__':
    sol = Solution()
    while True:
        lst = list(map(int, input('请输入数组：').split()))
        if not lst:
            exit(-1)
        print(sol.find_max_consecutive_ones(lst))
