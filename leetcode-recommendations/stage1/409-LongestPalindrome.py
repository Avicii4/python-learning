class Solution:
    def longest_palindrome(self, s: str) -> int:
        dct = {}
        for ch in s:
            dct[ch] = dct.get(ch, 0) + 1
        freqs = dct.values()
        sums, odd_flag = 0, False
        for n in freqs:
            if n % 2 == 0:
                sums += n
            else:
                odd_flag = True
                sums += n - 1
        return sums + (1 if odd_flag else 0)


if __name__ == '__main__':
    sol = Solution()
    while True:
        ss = input('输入字符串：')
        print('可生成的回文串最长为：{}'.format(sol.longest_palindrome(ss)))
