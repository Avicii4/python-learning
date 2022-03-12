from typing import List
from collections import Counter


class Solution:
    # 巨慢
    def find_special_integer_1(self, arr: List[int]) -> int:
        target = len(arr) // 4 + 1
        for num in set(arr):
            if arr.count(num) >= target:
                return num

    def find_special_integer_2(self, arr: List[int]) -> int:
        return Counter(arr).most_common(1)[0][0]

    # 很省时间
    def find_special_integer_3(self, arr: List[int]) -> int:
        n = len(arr)
        t = n // 4
        for i in range(n - t):
            if arr[i] == arr[i + t]:
                return arr[i]


if __name__ == '__main__':
    sol = Solution()
    arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
    print(sol.find_special_integer_2(arr))
