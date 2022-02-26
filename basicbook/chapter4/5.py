"""
输出一段英文文本中长度为3的单词
"""
import re

if __name__ == '__main__':
    s = "'Monday's child is fair of face, " \
        "Tuesday's child is full of grace, " \
        "Wednesday's child is full of woe, " \
        "Thursday's child has far to go," \
        "Friday's child is loving and giving," \
        "Saturday's child works hard for its living," \
        "And a child that's born on the Sabbath day" \
        "Is fair and wise and good and gay.'"

    pattern = r'\b[a-zA-z]{3}\b'
    print(re.findall(pattern, s))
