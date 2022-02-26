"""
递归判断一个字符串是否是回文
"""


def is_palindrome(s: str) -> bool:
    ll = len(s)
    if ll == 1 or ll == 0:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False


if __name__ == '__main__':
    while True:
        print(is_palindrome(input('输入字符串：')))
