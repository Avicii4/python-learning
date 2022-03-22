"""
输出 1000-9999 中满足以下条件的所有数：
1. 该数是素数
2. 十位数和个位数组成的数是素数，百位数和个位数组成的数是素数
3. 个位数和百位数组成的数是素数，个位数和十位数组成的数是素数
比如 1991 ，个位和十位组成的数就是 19
"""


def is_prime(n: int) -> bool:
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


if __name__ == '__main__':
    res = []
    for n in range(1001, 9999, 2):
        s = str(n)
        if is_prime(n) and is_prime(int(s[2] + s[3])) \
                and is_prime(int(s[1] + s[3])) and is_prime(int(s[3] + s[1])) \
                and is_prime(int(s[3] + s[2])):
            res.append(n)
    print(res)
