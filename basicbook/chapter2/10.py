"""
生成包含20个随机数的列表，
将前10个升序排序，后10个降序排序后输出
"""
from random import randint

if __name__ == '__main__':
    my_list = list(randint(-100, 100) for _ in range(20))
    print(my_list)
    print(sorted(my_list[:10]) + sorted(my_list[10:20], reverse=True))
