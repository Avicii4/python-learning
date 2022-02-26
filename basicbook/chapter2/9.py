"""
设计字典并支持用户输入取值
"""


def fun():
    a = ['a', 'b', 'c', 'd']
    b = list(range(1, 5))
    my_dict = dict(zip(a, b))
    key = input("请输入键值：")
    print(my_dict.get(key, "您输入的键不存在！"))


if __name__ == '__main__':
    while True:
        fun()
