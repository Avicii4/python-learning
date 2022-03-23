if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    res = set()
    for num in nums:
        s = list(str(num))
        res.add(eval('+'.join(s)))
    print(len(res))
    res = sorted(list(res))
    print(' '.join(map(str,res)))

