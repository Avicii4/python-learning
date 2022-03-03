from typing import List


class Solution:
    # 暴力比较所有距离
    def shortest_to_char_1(self, s: str, c: str) -> List[int]:
        n = len(s)
        res = [0] * n
        flags = [i for i in range(n) if s[i] == c]
        for i in range(n):
            res[i] = min(abs(i - j) for j in flags)
        return res

    def shortest_to_char_2(self, s: str, c: str) -> List[int]:

        # 二分法求i处于哪两个c的下标之间
        def locate(i: int, flags: List[int]) -> List[int]:
            low, high = 0, len(flags) - 1
            while low <= high:
                mid = (low + high) // 2
                if flags[mid] > i:
                    high = mid - 1
                elif flags[mid] < i:
                    low = mid + 1
            return [flags[low], flags[high]]

        n = len(s)
        flags = [i for i in range(n) if s[i] == c]
        res = []
        for i in range(n):
            if i in flags:
                res.append(0)
            elif i < flags[0]:
                res.append(flags[0] - i)
            elif i > flags[-1]:
                res.append(i - flags[-1])
            # 处于两个c之间
            else:
                loc = locate(i, flags)
                res.append(min(abs(loc[0] - i), abs(loc[1] - i)))
        return res

    def shortest_to_char_3(self, s: str, c: str) -> List[int]:
        prev, res = float('-inf'), []
        for i, v in enumerate(s):
            if v == c:
                prev = i
            res.append(i - prev)
        prev = float('inf')
        for i, v in enumerate(s[::-1]):
            n = len(s) - 1 - i
            if v == c:
                prev = n
            res[n] = min(prev - n, res[n])
        return res


if __name__ == '__main__':
    sol = Solution()
    while True:
        s = input('请输入字符串：')
        if not s:
            exit(-1)
        c = input('请输入字符：')
        print(sol.shortest_to_char_3(s, c))
