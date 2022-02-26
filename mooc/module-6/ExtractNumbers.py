"""
附件中有一个文本文件 strint.txt，该文件中有一段英文文章，在该文章中存在一些整数（有正有负）。
编写程序读取该文件、并提取出其中所有的整数，然后将这些整数中偶数位上全部为奇数的整数保存到
当前路径的 result.txt 文件中去，保存时每行3个数、每个数占8列、右对齐左补空格
"""
import re


def extract(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    pattern = re.compile(r'-?\d+')
    nums = pattern.findall(content)
    return nums


# 是否偶数位均是奇数
def is_valid(n):
    s = str(abs(int(n)))[::-1]
    if len(s) == 1:
        return False
    for i in range(1, len(s), 2):
        if int(s[i]) % 2 == 0:
            return False
    return True


def output(file, nums):
    nums = [n for n in nums if is_valid(n)]
    i = 0
    with open(file, 'w') as f:
        for n in nums:
            f.write(n.rjust(8))
            i += 1
            if i % 3 == 0:
                f.writelines('\n')


if __name__ == '__main__':
    output('files/result.txt', extract('files/strint.txt'))
