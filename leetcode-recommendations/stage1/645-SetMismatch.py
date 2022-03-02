from typing import List


class Solution:
    # 用字典记录频数
    def find_error_nums_1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dct = dict(zip(list(range(1, n + 1)), [0] * n))
        for i in nums:
            dct[i] = dct.get(i) + 1
        res = [0] * 2
        for i in dct:
            if dct[i] == 2:
                res[0] = i
            if dct[i] == 0:
                res[1] = i
        return res

    # 较法一更省空间，但搜索丢失数字的方法太费时间
    def find_error_nums_2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        for i in range(1, n + 1):
            if i not in nums:
                break
        dup = sum(nums) - n * (n + 1) // 2 + i
        return [dup, i]

    # 纯数学方法，时间最快
    def find_error_nums_3(self, nums: List[int]) -> List[int]:
        s, n = sum(nums), len(nums)
        dup = s - sum(set(nums))
        lost = n * (n + 1) // 2 + dup - s
        return [dup, lost]


if __name__ == '__main__':
    while True:
        sol = Solution()
        lst = list(map(int, input('输入数组：').split()))
        if not lst:
            exit(-1)
        print(sol.find_error_nums_3(lst))
