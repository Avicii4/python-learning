from math import sqrt


def is_prime(n: int) -> bool:
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def emirp(n: int) -> bool:
    if n <= 1:
        return False
    rev_n = int(str(n)[::-1])
    if rev_n == n:
        return False  # 回文数不是反素数
    return is_prime(n) and is_prime(rev_n)


if __name__ == '__main__':
    total = 30
    i = 0
    num = 2
    while total > 1:
        if emirp(num):
            print('{}'.format(num).rjust(5), end='')
            i += 1
            if i % 8 == 0:
                print()
            total -= 1
        num += 1
