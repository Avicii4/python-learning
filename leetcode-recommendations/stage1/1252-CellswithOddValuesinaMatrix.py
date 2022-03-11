from typing import List


class Solution:
    # 直观解法
    def odd_cells_1(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for indice in indices:
            for i in range(n):
                matrix[indice[0]][i] += 1
            for j in range(m):
                matrix[j][indice[1]] += 1
        return sum((x % 2 == 1 for x in (i for item in matrix for i in item)))

    # 算在indices中出现的次数
    def odd_cells_2(self, m: int, n: int, indices: List[List[int]]) -> int:
        row = [False for _ in range(m)]
        col = [False for _ in range(n)]
        # 每次加一都会改变奇偶性
        for r, c in indices:
            row[r] = not row[r]
            col[c] = not col[c]
        return sum((row[i] ^ col[j] for i in range(m) for j in range(n)))


if __name__ == '__main__':
    sol = Solution()
    m, n = 2, 2
    indices = [[0, 0], [1, 1]]
    print(sol.odd_cells_2(m, n, indices))
