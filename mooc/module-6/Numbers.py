"""
附件中有一个文本文件 numbers.txt，文件中的每一行都是一个浮点数，
编写程序读取出所有的浮点数。要求：
1 从小到大排序，将排序后的结果写到当前路径下新生成的一个文本文件
sort.txt 中，每个数占一行。
2 求出这些数字的均值、方差，将结果追加写到当前路径下新生成的一个
文本文件 sort.txt 中，每个数占一行。
3 要求生成的文本文件 sort.txt 中同时包含排序和均值、方差的结果。
"""


# 读取并排序
def read_sort(filename: str) -> list:
    with open(filename, 'r', encoding='utf-8') as f:
        nums = f.readlines()
    return sorted([float(n) for n in nums])


# 输出
def calc_output(filename: str, nums: list):
    avg = sum(nums) / len(nums)
    var = sum([(num - avg) ** 2 for num in nums]) / len(nums)
    with open(filename, 'a', encoding='utf-8') as f:
        f.write('有序序列：\n')
        for n in nums:
            f.write(str(n) + '\n')
        f.write('平均值：{}\n'.format(avg))
        f.write('方差：{}\n'.format(var))


if __name__ == '__main__':
    f1 = 'files/numbers.txt'
    f2 = 'files/sort.txt'
    calc_output(f2, read_sort(f1))
