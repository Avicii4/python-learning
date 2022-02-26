"""
用户输入一个列表和两个整数，
输出列表中介于这两个整数下标的子列表
"""


def fun1():
    arr = input("请输入一个列表：").split(',')
    arr = list(map(int, arr))
    print(arr)
    a = int(input("请输入一个整数："))
    b = int(input("请输入一个整数："))
    print(arr[a:b + 1])


def fun2():
    num_list = eval(input("输入[1,2,3,4,5]形式的列表:"))
    start, end = map(int, input("输入形如1,2的两个整数：").split(','))
    print(num_list[start:end + 1])


if __name__ == '__main__':
    fun2()
