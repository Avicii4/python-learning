"""
输出一个字符串的所有字串
"""


# 递归
def print_all_subs(string: str, idx: int, res: str):
    if idx == len(string):
        print(res)
    else:
        # 选择要[i]
        print_all_subs(string, idx + 1, res)
        # 选择不要[i]
        print_all_subs(string, idx + 1, res + string[idx])


if __name__ == '__main__':
    print_all_subs('ABCDE', 0, '')
