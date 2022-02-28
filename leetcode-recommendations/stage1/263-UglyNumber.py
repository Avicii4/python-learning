class Solution:
    def is_ugly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            if n % 2 == 0:
                n //= 2
            elif n % 3 == 0:
                n //= 3
            elif n % 5 == 0:
                n //= 5
            else:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    while True:
        x = int(input('请输入整数：'))
        print(sol.is_ugly(x))
