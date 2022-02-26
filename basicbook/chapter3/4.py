"""
生成一个包含50个随机整数的列表，删除其中的奇数
"""
from random import randint

if __name__ == '__main__':
    random_list = list(randint(0, 100) for _ in range(50))
    for i in range(len(random_list))[::-1]:    # 从列表最后开始删除
        if random_list[i] % 2 == 1:
            # random_list.pop(i)
            del random_list[i]
    print(random_list)
