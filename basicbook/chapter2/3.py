# 生成1000个0~100之间的随机整数，统计每个元素出现的次数
import random

if __name__ == '__main__':
    rlist = [random.randint(0, 100) for _ in range(1000)]
    print(rlist)
    # 创建只有键值的字典
    freq_dict = dict.fromkeys(range(101), 0)
    for i in rlist:
        freq_dict[i] += 1
    print(freq_dict)

