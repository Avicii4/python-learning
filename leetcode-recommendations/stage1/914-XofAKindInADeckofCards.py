from typing import List
from collections import Counter
from functools import reduce
from math import gcd


class Solution:
    # 判断各数的频次是否有公因数
    def has_groups_size_x_1(self, deck: List[int]) -> bool:
        def has_common_factor(a: int, b: int) -> bool:
            if a < b:
                a, b = b, a
            while b:
                a, b = b, a % b
            return a >= 2

        vals = dict(Counter(deck)).values()
        nums = list(set(vals))
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if not has_common_factor(nums[i], nums[j]):
                    return False
        return True

    # 用reduce求所有数的最大公因数
    def has_groups_size_x_2(self, deck: List[int]) -> bool:
        vals = Counter(deck).values()
        return reduce(gcd, vals) >= 2


if __name__ == '__main__':
    sol = Solution()
    de = [1, 2, 3, 4, 4, 3, 2, 1]
    print(sol.has_groups_size_x_2(de))
