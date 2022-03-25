if __name__ == '__main__':
    m = int(input())
    nums = list(map(int, input().split()))
    for k in nums:
        for n in range(1, 10):
            p = len(str(k))
            if (n * k ** 2) % 10 ** p == k:
                print(n, n * k ** 2)
                break
        else:
            print('No')


