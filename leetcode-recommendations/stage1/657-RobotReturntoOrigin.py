class Solution:
    def judge_circle(self, moves: str) -> bool:
        return moves.count('L') == moves.count('R') \
               and moves.count('U') == moves.count('D')


if __name__ == '__main__':
    sol = Solution()
    while True:
        s = input('请输入移动字符串:')
        if not s:
            exit(-1)
        print(sol.judge_circle(s))
