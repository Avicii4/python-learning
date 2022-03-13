"""
这次尽量做优化也不能100%AC，也不能调sympy库
"""
if __name__ == '__main__':
    n = int(input())
    if n < 5:
        print(0)
    primes = [2]
    for num in range(3, n + 1, 2):
        for i in range(3, int(num ** 0.5) + 1):
            if not num % i:
                break
        else:
            primes.append(num)
    res = 0
    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] == 2:
            res += 1
    print(res)
