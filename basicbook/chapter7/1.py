"""
读取一个英文文本en.txt，并将其大小写字母互换
"""

if __name__ == '__main__':
    fp = open('files/en.txt', 'r+')
    lines = fp.readlines()
    print('转换前：' + str(lines))
    fp.seek(0)
    for i, v in enumerate(lines):
        v = v.swapcase()
        lines[i] = v
        fp.write(v)
    print('转换后：' + str(lines))
    fp.close()
