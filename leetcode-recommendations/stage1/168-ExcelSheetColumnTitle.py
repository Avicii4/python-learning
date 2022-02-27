import string


class Solution:
    def convert_to_title(self, column_number: int) -> str:
        letters = string.ascii_uppercase
        res = str()
        while column_number > 0:
            m = column_number % 26
            s = 'Z' if m == 0 else letters[m - 1]
            res = s + res
            column_number -= 1
            column_number //= 26
        return res


if __name__ == '__main__':
    sol = Solution()
    while True:
        p = int(input('请输入整数：'))
        print(sol.convert_to_title(p))
