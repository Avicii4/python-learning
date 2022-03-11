from typing import List

"""
给定一个数组arr和整数aim，任意选择arr中的数字，
能否相加得aim，返回 True 或 False
"""


# 暴力递归
def violent(arr: List[int], aim: int, idx: int, cur: int) -> bool:
    if idx == len(arr):
        return cur == aim
    else:
        # 选择加或不加上当前的arr[idx]
        return violent(arr, aim, idx + 1, cur) or violent(arr, aim, idx + 1, cur + arr[idx])


# 改dp(不含负数)
def dynamic(arr: List[int], aim: int) -> bool:
    m, n = len(arr), sum(arr)
    dp = [[False for _ in range(n + 1)] for _ in range(m)]
    for i in range(m):
        dp[i][aim] = True
    for i in range(m - 2, -1, -1):
        for j in range(aim, -1, -1):
            if j + arr[i] > n - 1:
                dp[i][j] = dp[i + 1][j]
            else:
                dp[i][j] = dp[i + 1][j] or dp[i + 1][j + arr[i] + 1]
    return dp[0][0]


if __name__ == '__main__':
    nums = [2, 0, 9, 1]
    # print(violent(nums, -18, 0, 0))
    print(dynamic(nums, 11))
