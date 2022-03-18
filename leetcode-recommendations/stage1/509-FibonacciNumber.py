class Solution:
    # 递归
    def fib_1(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib_1(n - 1) + self.fib_2(n - 2)

    # 迭代
    def fib_2(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        a, b = 0, 1
        while n >= 2:
            a, b = b, a + b
            n -= 1
        return b


if __name__ == '__main__':
    sol = Solution()
    while True:
        x = int(input('请输入一个自然数：'))
        print(sol.fib_2(x))
