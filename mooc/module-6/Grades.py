"""
data.txt中存储了n个同学的信息
每个同学占一行，分别是姓名、性别、选择题成绩、编程题成绩
其中性别0表示男生、1表示女生
选择题成绩和编程题成绩都是100分制。
要求如下：
1.读取出文件中的所有信息到列表
2.删除考试成绩不合法的同学，然后显示剩余人数
3.对列表的信息按照总评成绩进行排序，具体描述
     A 总评成绩时，选择题占20%，编程题占80%
     B 按照总评成绩从高到低排序
     C 当总评成绩相同时，女士优先
4.显示排序后的结果，每人一行，输出至rank.txt，显示要求
     姓名（占20列，左对齐），性别（要求显示Male或Female，占10列，左对齐），总评成绩（小数点后面保留1位，占5列，左对齐）
"""


def rank_students():
    with open('files/data.txt', 'r', encoding='utf-8') as f1:
        data = f1.readlines()
    data = [d.strip() for d in data if d.strip()]  # 去空行
    data_list = []
    for d in data:
        r = d.split(',')
        choice, program = int(r[2]), int(r[3])
        if 0 <= choice <= 100 and 0 <= program <= 100:  # 剔除问题数据
            r[2], r[3] = choice, program
            data_list.append(r)
    rank_list = []
    for d in data_list:
        d[2] = 0.2 * d[2] + 0.8 * d[3]
        d.pop()
        rank_list.append(d)
    with open('files/rank.txt', 'w', encoding='utf-8') as f2:
        f2.write('Total valid data:{}\n'.format(len(rank_list)))
        for i in sorted(rank_list, key=lambda x: (x[2], x[1]), reverse=True):  # 排序的两大条件
            f2.write('{}'.format(i[0]).ljust(20))
            f2.write('{}'.format('Male' if i[1] == '0' else 'Female').ljust(10))
            f2.write('{:.1f}\n'.format(i[2]).ljust(5))


if __name__ == '__main__':
    rank_students()
