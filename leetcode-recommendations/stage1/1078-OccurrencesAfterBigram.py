from typing import List


class Solution:
    def find_ocurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        n, res = len(text), []
        for i in range(n - 2):
            if text[i] == first and text[i + 1] == second:
                res.append(text[i + 2])
        return res


if __name__ == '__main__':
    sol = Solution()
    first, second = 'we', 'will'
    text = 'we will we will rock you'
    print(sol.find_ocurrences(text, first, second))
