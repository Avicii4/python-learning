from typing import List


class Solution:
    # 太丑了
    def fair_candy_swap_1(self, alice_sizes: List[int], bob_sizes: List[int]) -> List[int]:
        a, b = sum(alice_sizes), sum(bob_sizes)
        offset = abs(a - b) // 2
        alice_sizes.sort()
        bob_sizes.sort()
        if a > b:
            for i in alice_sizes:
                if i - offset in bob_sizes:
                    return [i, i - offset]
        else:
            for i in alice_sizes:
                if i + offset in bob_sizes:
                    return [i, i + offset]

    def fair_candy_swap_2(self, alice_sizes: List[int], bob_sizes: List[int]) -> List[int]:
        a, b = sum(alice_sizes), sum(bob_sizes)
        delta = (a - b) // 2
        # 这一步削减数组长度
        rec = set(alice_sizes)
        for y in set(bob_sizes):
            x = y + delta
            if x in rec:
                return [x, y]

