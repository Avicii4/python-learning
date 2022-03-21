"""
把 10 到 1000 之间满足以下两个条件的数，存到 2007.txt 文件中.
1. 是素数
2. 它的反数也是素数，如：123 的反数是 321
"""


def is_prime(n: int) -> bool:
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


if __name__ == '__main__':
    res = []
    t = [11, 13, 17, 31, 37, 71, 73, 79, 97, 101, 107, 113, 131, 149, 151, 157,
         167, 179, 181, 191, 199, 311, 313, 337, 347, 353, 359, 373, 383, 389,
         701, 709, 727, 733, 739, 743, 751, 757, 761, 769, 787, 797, 907, 919,
         929, 937, 941, 953, 967, 971, 983, 991]
    for i in range(11, 1000, 2):
        if is_prime(i) and is_prime(int(str(i)[::-1])):
            res.append(str(i))
    with open('file/2007.txt', 'w', encoding='utf-8') as f:
        for num in res:
            f.write(num + '\n')
