from typing import List

"""
给定数组arr，arr中所有的值都为正数且不重复。每个值代表一种面值的货币，
每种面值的货币可以使用任意张，再给定一个整数aim代表要找的钱数，求换钱有多少种方法?
举例:
1. arr=[5,10,25,1]，aim=0。组成0元的方法有1种，就是所有面值的货币都不用。所以返回1。
2. arr=[5,10,25,1],aim=15。组成15元的方法有6种，
分别为：3张5元、1张10元+1张5元、1张10元+5张1元、10张1元+1张5元、2张5元+5张1元和15张1元。所以返回6。
3. arr=[3,5]，aim=2。任何方法都无法组成2元。所以返回0。
"""


def violent(arr: List[int], aim: int, index: int) -> int:
    """
    暴力递归法
    :param arr: 货币面额数组
    :param aim: 目标钱数
    :param index: 可使用index及其之后位置的钱币
    :return: 换钱方法数
    """
    res = 0
    if index == len(arr):
        res = 1 if aim == 0 else 0
    else:
        for i in range(aim // arr[index] + 1):
            res += violent(arr, aim - i * arr[index], index + 1)
    return res


def dynamic(arr: List[int], aim: int) -> int:
    dp = [[0 for _ in range(aim + 1)] for _ in range(len(arr))]
    for i in range(len(arr)):
        dp[i][0] = 1
    for i in range(1, aim // arr[0] + 1):
        dp[0][arr[0] * i] = 1
    for i in range(1, len(arr)):
        for j in range(1, aim + 1):
            dp[i][j] = dp[i - 1][j]
            if j - arr[i] >= 0:
                dp[i][j] += dp[i][j - arr[i]]
    return dp[len(arr)-1][aim]


if __name__ == '__main__':
    arr = [5, 10, 25, 1]
    # print(violent(arr, 15, 0))
    print(dynamic(arr, 15))
