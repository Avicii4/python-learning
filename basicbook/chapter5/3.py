"""
函数接收一个字符串，统计大写、小写、数字和其他字符
"""


def string_count(s):
    types = [0, 0, 0, 0]
    for i in s:
        if 'A' <= i <= 'Z':
            types[0] += 1
        elif 'a' <= i <= 'z':
            types[1] += 1
        elif '0' <= i <= '9':
            types[2] += 1
        else:
            types[3] += 1
    print({'大写字母：': types[0], '小写字母：': types[1], '数字：': types[2], '其他：': types[3]})


if __name__ == '__main__':
    string_count('3yehd7_823h  ^4fd')
