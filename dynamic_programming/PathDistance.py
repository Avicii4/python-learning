from typing import List

"""
一个二维数组，每一格都有一个权重，要求从左上角走到右下角，
且每次只能向下或向右，输出行走的最小路径和
例如：
3 2 1 1
7 5 1 1
3 4 6 2
输出：10
"""


# 暴力递归
def violent(path: List[List[int]], i: int, j: int, cur: int) -> int:
    cur += path[i][j]
    if i == len(path) - 1 and j == len(path[0]) - 1:
        return cur
    elif i == len(path) - 1:
        return violent(path, i, j + 1, cur)
    elif j == len(path[0]) - 1:
        return violent(path, i + 1, j, cur)
    else:
        return min(violent(path, i + 1, j, cur), violent(path, i, j + 1, cur))


# 无后效性问题改dp
def dynamic(path: List[List[int]]):
    m, n = len(path), len(path[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    # 最右下角的结果
    dp[m - 1][n - 1] = path[m - 1][n - 1]
    # 最后一行的结果
    for i in range(n - 2, -1, -1):
        dp[m - 1][i] = dp[m - 1][i + 1] + path[m - 1][i]
    # 最后一列的结果
    for i in range(m - 2, -1, -1):
        dp[i][n - 1] = dp[i + 1][n - 1] + path[i][n - 1]
    # 最后从右到左、从下到上填充dp
    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + path[i][j]
    return dp[0][0]


if __name__ == '__main__':
    path = [[3, 2, 1, 1], [7, 5, 1, 1], [3, 4, 6, 2]]
    # print(violent(path, 0, 0, 0))
    print(dynamic(path))
