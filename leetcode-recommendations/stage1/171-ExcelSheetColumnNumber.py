import string


class Solution:
    def title_to_number(self, column_title: str) -> int:
        letters = string.ascii_uppercase
        res = 0
        l = len(column_title)
        for i in range(l):
            index = letters.find(column_title[i]) + 1
            res += index * (26 ** (l - 1 - i))
        return res


if __name__ == '__main__':
    sol = Solution()
    while True:
        s = input('输入序号：')
        print(sol.title_to_number(s))
