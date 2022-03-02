from typing import List


class Solution:
    def distribute_candies(self, candy_type: List[int]) -> int:
        return min(len(set(candy_type)), len(candy_type) // 2)


if __name__ == '__main__':
    sol = Solution()
    candyType = [6,6,6,6]
    print(sol.distribute_candies(candyType))
