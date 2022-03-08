from typing import List
import heapq


class Solution:
    def last_stone_weight_1(self, stones: List[int]) -> int:
        while len(stones) > 1:
            y = max(stones)
            stones.remove(y)
            x = max(stones)
            stones.remove(x)
            if x < y:
                stones.append(y - x)
        return 0 if len(stones) == 0 else stones[0]

    def last_stone_weight_2(self, stones: List[int]) -> int:
        # heapq默认创建小根堆，故先取相反数
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            y, x = heapq.heappop(stones), heapq.heappop(stones)
            if x < y:
                heapq.heappush(stones, y - x)
        return -stones[0] if stones else 0


if __name__ == '__main__':
    sol = Solution()
    while True:
        arr = list(map(int, input('请输入数组：').split()))
        if not arr:
            exit(-1)
        print(sol.last_stone_weight(arr))
