"""
找出 100 到 1000 内的不含 9 的素数, 存到 2006.txt 文件中.
"""


def is_prime(n: int) -> bool:
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


if __name__ == '__main__':
    res = []
    for i in range(101, 1000, 2):
        if is_prime(i) and '9' not in str(i):
            res.append(str(i))
    with open('file/2006.txt', 'w+', encoding='utf-8') as f:
        for num in res:
            f.write(num)
            f.write('\n')
