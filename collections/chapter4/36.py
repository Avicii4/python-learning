from math import sqrt


def is_prime(n: int) -> bool:
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_mason(n: int) -> int:
    if is_prime(n) and n & (n - 1) == 0:
        return len(bin(n)) - 3
    return -1


if __name__ == '__main__':
    for i in range(2, 10):
        x = 2 ** i - 1
        if is_prime(x):
            print('{}'.format(i).rjust(3) + '{}'.format(x).rjust(4))
