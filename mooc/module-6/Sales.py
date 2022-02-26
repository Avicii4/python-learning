"""
现有一个文本文件sales.txt，其中存储了一些同学在食堂的消费信息
编写程序实现如下功能：
1.显示其中合计有多少条记录；
2.显示其中合计涉及多少人；
3.统计出每人的消费，并从高到低排序。
4.输出排序结果到res.txt，要求每人信息一行，学号和金额之间用逗号分开，每人的金额小数点后面保留两位
"""


def sales_data():
    with open('files/sales.txt', 'r', encoding='utf-8') as f1:
        records = f1.readlines()
    dct = dict()
    for record in records:
        r = record.split()
        dct[r[0]] = dct.get(r[0], 0.0) + float(r[1])

    with open('files/res.txt', 'w', encoding='utf-8') as f2:
        f2.write('Total records:{}\n'.format(len(records)))
        f2.write('Total students:{}\n'.format(len(dct)))
        f2.write('Sorted by sales:\n')
        for item in sorted(dct, key=lambda x: dct[x], reverse=True):
            f2.write('{}, {:.2f}\n'.format(item, dct[item]))


if __name__ == '__main__':
    sales_data()
