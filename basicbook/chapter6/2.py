"""
设计一个三维向量类，实现向量加法、减法，以及与数的乘除法
"""


class Vector:
    __value = []
    size = 0

    # 判断元素是不是数字
    def __is_number(self, n):
        if (not isinstance(n, int)) and (not isinstance(n, float)) and (not isinstance(n, complex)):
            return False
        return True

    # 输入参数初始化
    def __init__(self, *args):
        if not args:
            self.__value = []
        else:
            for arg in args:
                if not self.__is_number(arg):
                    print('向量元素不合法')
                    return
            self.__value = list(args)

    # 求向量维数
    def __len__(self):
        return len(self.__value)

    # 向量加法
    def __add__(self, n):
        if not isinstance(n, Vector):
            print('请输入一个向量')
            return
        if len(n.__value) != len(self.__value):
            print('向量维数不同，无法相加')
        tmp = Vector()
        for i, j in zip(self.__value, n.__value):
            tmp.__value.append(i + j)
        return tmp

    # 向量减法
    def __sub__(self, n):
        if not isinstance(n, Vector):
            print('请输入一个向量')
            return
        if len(n.__value) != len(self.__value):
            print('向量维数不同，无法相减')
        tmp = Vector()
        for i, j in zip(self.__value, n.__value):
            tmp.__value.append(i - j)
        return tmp

    # 数乘
    def __mul__(self, n):
        if not self.__is_number(n):
            print('请输入一个数')
            return
        tmp = Vector()
        for v in self.__value:
            tmp.__value.append(v * n)
        return tmp

    # 数除
    def __truediv__(self, n):
        if not self.__is_number(n):
            print('请输入一个数')
            return
        tmp = Vector()
        for v in self.__value:
            tmp.__value.append(v / n)
        return tmp

    @classmethod
    def show(cls, n):
        print(list(n.__value))


if __name__ == '__main__':
    x = Vector(1, 2, 3, 4, 5)
    y = Vector(6, 7, 8, 9, 10)
    Vector.show(x + y)
    Vector.show(y - x)
    Vector.show(x * 3)
    Vector.show(y / 2)
