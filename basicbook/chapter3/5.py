"""
生成一个包含20个随机整数的列表，
然后对其偶数下标的元素进行降序排序，奇数下标的元素位置不变。
"""
from random import randint

if __name__ == '__main__':
    random_list = list(randint(0, 100) for _ in range(20))
    print('排序前：', random_list)
    # 只写 sorted(random_list[::2], reverse=True) 是错误的，只会输出一半
    random_list[::2] = sorted(random_list[::2], reverse=True)
    print('排序后：', random_list)
