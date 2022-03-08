from typing import List


class Solution:
    def valid_mountain_array(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3 or arr[0] >= arr[1] or arr[-1] >= arr[-2]:
            return False
        i = 0
        while arr[i] < arr[i + 1]:
            i += 1
        while i < n - 1 and arr[i] > arr[i + 1]:
            i += 1
        return i == n - 1


if __name__ == '__main__':
    sol = Solution()
    while True:
        nums = list(map(int, input('请输入数组：').split()))
        if not nums:
            exit(-1)
        print(sol.valid_mountain_array(nums))
