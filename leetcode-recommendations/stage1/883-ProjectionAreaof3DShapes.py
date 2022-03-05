from typing import List


class Solution:
    def projection_area(self, grid: List[List[int]]) -> int:
        # area[0]: 非0元素的数量
        # area[1]: grid转置后每个子list中的最大值
        # area[2]: 每个子list中的最大值
        area = [0] * 3
        n = len(grid)
        plain = [i for item in grid for i in item]
        for k in range(n):
            area[1] += max(plain[k::n])
        area[0] = sum([bool(x) for x in plain])
        area[2] = sum([max(lst) for lst in grid])
        return sum(area)


if __name__ == '__main__':
    sol = Solution()
    grids = [[2, 3], [2, 4]]
    print(sol.projection_area(grids))
