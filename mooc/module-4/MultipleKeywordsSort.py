"""
使用Python的sort方法和sorted函数进行多关键字排序时
• 先对次关键字排序，再对主关键字排序
• 主关键字相同，不会改变次关键字决定的顺序
"""
if __name__ == '__main__':
    l = [('摩洛哥', 2, 2, 0, 1),
         ('葡萄牙', 5, 4, 1, 5),
         ('西班牙', 6, 5, 1, 5),
         ('伊朗', 2, 2, 0, 4)]
    l.sort(key=lambda t: t[1], reverse=True)
    l.sort(key=lambda t: t[3], reverse=True)
    l.sort(key=lambda t: t[4], reverse=True)
    print(list(t[0] for t in l))
