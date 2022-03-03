class Solution:
    def num_jewels_in_stones_1(self, jewels: str, stones: str) -> int:
        res = 0
        for stone in stones:
            if stone in jewels:
                res += 1
        return res

    def num_jewels_in_stones_2(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        # True为1，False为0，因此这个生成器也可以求和，妙
        return sum(stone in jewel_set for stone in stones)


if __name__ == '__main__':
    sol = Solution()
    js = 'aA'
    s = 'Azsdza'
    print(sol.num_jewels_in_stones_2(js, s))
