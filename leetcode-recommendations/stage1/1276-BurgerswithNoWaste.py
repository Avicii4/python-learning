from typing import List


class Solution:
    # 求二元一次方程的非负整数解
    def num_of_burgers(self, tomato_slices: int, cheese_slices: int) -> List[int]:
        y = (4 * cheese_slices - tomato_slices) / 2
        if 0 <= y == int(y):
            y = int(y)
            x = cheese_slices - y
            if x >= 0:
                return [x, y]
        return []


if __name__ == '__main__':
    sol = Solution()
    print(sol.num_of_burgers(4007112, 1457628))
