"""
2014_in.txt 中有一堆整型数字，每次读取两个，这两个数构成一个坐标。
1. 规定处于第一象限的数是有效点(即 x>0, y>0 的坐标)，问这么多点中有效点有多少个？
2. 现在用户从键盘输入一个坐标和一个数字 k ，设计算法输出 k 个离该坐标距离最近的点
的坐标和每个坐标到该点的距离，写入到 2014_out.txt 文件中。
"""
if __name__ == '__main__':
    with open('file/2014_in.txt', 'rt', encoding='utf-8') as f:
        content = f.read().split()
    points = [(int(content[i]), int(content[i + 1])) for i in range(0, len(content), 2)]
    valid = [p for p in points if p[0] > 0 and p[1] > 0]

    # 可能要考虑 k 超过len(valid)
    x, y, k = map(int, input('请输入一个坐标和一个整数（共三个整数）：').split())
    distance = [(i, ((x - p[0]) ** 2 + (y - p[1]) ** 2) ** 0.5) for i, p in enumerate(valid)]
    distance.sort(key=lambda k: k[1])
    res = []
    for i in range(k):
        res.append('{} {}'.format(valid[distance[i][0]], distance[i][1]))
    with open('file/2014_out.txt', 'w', encoding='utf-8') as f:
        f.write('有效点共{}个\n'.format(len(valid)))
        f.write('这些点距离({},{})最近的{}个及距离是：\n'.format(x, y, k))
        for elem in res:
            f.write(elem + '\n')
