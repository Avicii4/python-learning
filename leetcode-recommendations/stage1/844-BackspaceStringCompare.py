from typing import List


class Solution:
    def backspace_compare(self, s: str, t: str) -> bool:
        # 善用栈，有点类似计算后缀表达式
        def generate(s: str) -> List[str]:
            stack = list()
            for ch in s:
                if ch != '#':
                    stack.append(ch)
                elif stack:
                    stack.pop()
            return stack

        return generate(s) == generate(t)


if __name__ == '__main__':
    sol = Solution()
    while True:
        ss = input('请输入字符串一：')
        if not ss:
            exit(-1)
        tt = input('请输入字符串二：')
        print(sol.backspace_compare(ss, tt))
