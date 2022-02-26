"""
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词
"""


# 用关键词 in
def is_same_line_1(s: str) -> bool:
    s = s.lower()
    line1 = 'qwertyuiop'
    line2 = 'asdfghjkl'
    line3 = 'zxcvbnm'
    keyborad = [line1, line2, line3]
    for i in range(3):
        if all(ch in keyborad[i] for ch in s):
            return True
    return False


# 用集合比大小的特性
def is_same_line_2(s: str) -> bool:
    line1 = set('qwertyuiop')
    line2 = set('asdfghjkl')
    line3 = set('zxcvbnm')
    set_s = set(s.lower())
    return set_s < line1 or set_s < line2 or set_s < line3


if __name__ == '__main__':
    L = ['pop', 'key', 'had', 'visit']
    print([word for word in L if is_same_line_2(word)])
