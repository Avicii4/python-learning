class Solution:
    def find_complement_1(self, num: int) -> int:
        lst = list(bin(num)[2:])
        n = len(lst)
        for i in range(n):
            lst[i] = '1' if lst[i] == '0' else '0'
        return int(''.join(lst), 2)

    # 此法Python运行起来较慢，不如其他语言，也不如法一，但用到了位运算
    def find_complement_2(self, num: int) -> int:
        c = 1
        while True:
            if num >= c:
                c *= 2
            else:
                return c - num - 1


if __name__ == '__main__':
    sol = Solution()
    while True:
        p = int(input('请输入一个整数：'))
        print(sol.find_complement_2(p))
