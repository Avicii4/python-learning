from typing import List


class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        res = []
        for i in range(num_rows):
            data = [0] * (i + 1)
            data[0] = data[i] = 1
            for j in range(1, i):
                data[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(data)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.generate(0))
    print(sol.generate(5))
    print(sol.generate(1))
