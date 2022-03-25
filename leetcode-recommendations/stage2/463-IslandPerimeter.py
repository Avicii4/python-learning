from typing import List


class Solution:
    def island_perimeter(self, grid: List[List[int]]) -> int:
        land = cnt = 0
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    land += 1
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        cnt += 1
                    if i + 1 < row and grid[i + 1][j] == 1:
                        cnt += 1
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        cnt += 1
                    if j + 1 < col and grid[i][j + 1] == 1:
                        cnt += 1
        return 4 * land - cnt


if __name__ == '__main__':
    sol = Solution()
    g = [[0, 1, 0, 0]]
    print(sol.island_perimeter(g))
