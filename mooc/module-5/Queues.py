"""
小明将学生排队，学号小到大排一排，然后进行多次调整
一次调整可能让一名同学出队 向前或先后移动一段距离再入队

例：学生人数8人
0）初始 1，2，3，4，5，6，7，8
1）第一次调整 3号向后移动2 -> 1，2，4，5，3，6，7，8

函数接收两个参数：
m:学生的数量
lst:每一个元素是一个元组，元组的第一个元素是学号，第二个是移动的数量，负数表示向前
输出：
返回一个列表，按照顺序存储了当前位置上学生的学号
"""


def move(m, lst):
    students = [i for i in range(1, m + 1)]
    for item in lst:
        index = students.index(item[0])  # 学号是item[0] 的学生的下标
        student = students.pop(index)
        index += item[1]  # 目标位置下标
        if 0 <= index < m:
            students.insert(index, student)
        elif item[1] > 0:  # 超过队长，放在队尾
            students.append(student)
        elif item[1] < 0:
            students.insert(0, student)
    return students


if __name__ == '__main__':
    num = 8
    lst = [(3, 2), (8, -1), (7, -6)]
    print(move(num, lst))
