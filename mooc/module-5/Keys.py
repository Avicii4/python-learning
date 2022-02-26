"""
车队有一个公共钥匙盒
有N个挂钩，用来挂N把钥匙，二者都有编号
每次借钥匙只取指定钥匙，不移动其余钥匙
每次还钥匙，还在最左边的空位挂钩上
- 如果同一时刻有借有还，那么先还后借
- 如果同一时刻多个还，按照钥匙编号顺序还
开始N把钥匙是按编号从小到大存放
有K条钥匙借用记录（三个部分）
钥匙编号借用时间使用时长
请按顺序输出最终钥匙盒里面的钥匙编号

- 样例输入:
5 2
4 3 3
2 2 7
- 样例说明:
• 合计有5把钥匙，2条借用记录
• 4号钥匙在时刻3被借用，使用3个单位时间，也就是时刻6还钥匙
• 2号钥匙在时刻2被借用，使用7个单位时间，也就是时刻9还钥匙

方法：
• 每一条借还记录包括借操作和还操作
    • 借的时刻在前
    • 还的时刻在后
    • 因此模拟时一条数据要被处理两次
• 直接把一条记录拆分成两条记录
    • 钥匙编号 时刻 借操作
    • 钥匙编号 时刻 还操作
"""


def solution():
    key_count, row_count = map(int, input().split())  # 取第一行两个数据

    keys = [i for i in range(1, key_count + 1)]  # 初始化钥匙序列
    datas = []
    for i in range(row_count):
        temp = list(map(int, input().split()))
        datas.append([temp[0], temp[1], 1])  # 借出记录
        datas.append([temp[0], temp[1] + temp[2], 2])  # 返还记录，计算返还的时刻

    datas.sort(key=lambda t: (t[1], -t[2], t[0]))  # 按借出时间先后、借记录前还记录后、钥匙编号进行排序
    print(datas)

    for item in datas:
        if item[2] == 1:  # 借记录
            keys[keys.index(item[0])] = 0  # 对应钥匙置零
        else:
            keys[keys.index(0)] = item[0]  # 最小位置处放上钥匙

    for item in keys:
        print(item, end=' ')


if __name__ == '__main__':
    solution()
