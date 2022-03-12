from typing import List


class Solution:
    def k_weakest_rows(self, mat: List[List[int]], k: int) -> List[int]:
        lst = [(i, sum(lst)) for i, lst in enumerate(mat)]
        return [x[0] for x in sorted(lst, key=lambda t: t[1])][:k]


if __name__ == '__main__':
    sol = Solution()
    mat = [[1, 1, 0, 0, 0],
           [1, 1, 1, 1, 0],
           [1, 0, 0, 0, 0],
           [1, 1, 0, 0, 0],
           [1, 1, 1, 1, 1]]
    print(sol.k_weakest_rows(mat, 3))
