"""
对下列文字进行词频统计，再按照词频和字典顺序排序
词频是主关键字，字典顺序是次关键字，字典顺序不考虑大小写
"""

if __name__ == '__main__':
    s = """
    Python includes two operations for sorting. The method sort() in the built-in list data type
    rearranges the items in the underlying list into ascending order, much like merge.sort(). In
    contrast, the built-in function sorted() leaves the underlying list alone; instead, it returns a
    new list containing the items in ascending order.
    """
    # s = s.replace('()', ' ')
    # s = s.replace('.', ' ')
    # s = s.replace(',', '')
    s = s.translate(''.maketrans('().,', '    '))   # maketrans()前后参数长度保持一致
    data = s.split()
    d = dict()
    for word in data:
        d[word] = d.get(word, 0) + 1

    print('词频统计结果：')
    index = 0
    for kv in d.items():  # 按照初始顺序打印
        print(kv, end='\t')
        index += 1
        if index % 6 == 0:
            print()

    d1_list = sorted(d.items(), key=lambda w: w[0].lower())  # 按照键值对中的key排序，且忽略大小写
    # d1_list是一个list，其中成员均为tuple类型
    print('---------------------------------\n排序后结果:')
    index = 0
    for kv in sorted(d1_list, key=lambda w: w[1], reverse=True):  # 按键值对中的value倒序
        print(kv, end='\t')
        index += 1
        if index % 6 == 0:
            print()


# TODO l.sort()直接在内存上动手脚
# sorted()第一个参数可以是tuple，但返回的是list
