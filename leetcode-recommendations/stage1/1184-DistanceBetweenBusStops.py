from typing import List


class Solution:
    def distance_between_bus_stops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        n = sum(distance[start:destination])
        m = sum(distance[:start])+sum(distance[destination:])
        return min(n, m)


if __name__ == '__main__':
    sol = Solution()
    dis = [1, 2, 3, 4]
    print(sol.distance_between_bus_stops(dis, 0, 2))
