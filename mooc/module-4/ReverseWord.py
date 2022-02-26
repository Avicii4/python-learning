"""
给定一个字符串，你需要反转字符串中每个单词的字符顺序，
同时仍保留空格和单词的初始顺序。

输入: "Let's take LeetCode contest"

输出: "s'teL ekat edoCteeL tsetnoc"

注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
"""


def reverse(s: str) -> str:
    words = s.split()
    new_words = list(map(lambda x: x[::-1], words))
    return ' '.join(new_words)
    # 一行 ：  return ' '.join(list(map(lambda x: x[::-1], s.split())))


if __name__ == '__main__':
    string = 'Let\'s take LeetCode contest'
    print(reverse(string))
