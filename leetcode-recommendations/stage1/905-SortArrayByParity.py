from typing import List


class Solution:
    def sort_array_by_parity(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: x % 2)
        return nums


if __name__ == '__main__':
    sol = Solution()
    arr = [1, 3, 7, 4, 6, 8]
    print(sol.sort_array_by_parity(arr))
