"""
统计文件test.txt中字母的出现频率
"""
if __name__ == '__main__':
    fp = open('test.txt', 'rt')  # TODO 只读常用rt
    data = fp.readlines()
    fp.close()
    d = dict()
    for line in data:
        line = line.upper()
        for ch in line:
            if 'A' <= ch <= 'Z':
                d[ch] = d.get(ch, 0) + 1
    index = 0

    # 按key正序输出
    for i in sorted(d):
        print('{0}:{1}'.format(i, d[i]), end='  \t')
        index += 1
        if index % 4 == 0:
            print()

    print('\n----------------')

    # 按value倒序输出
    index = 0
    for i in sorted(d, key=lambda x: d[x], reverse=True):  # TODO 字典按照value排序的写法
        print('{0}:{1}'.format(i, d[i]), end='  \t')
        index += 1
        if index % 4 == 0:
            print()
