if __name__ == '__main__':
    arr = list(map(int, input().split()))
    res = []
    for i in range(0, len(arr) - 1, 2):
        if arr[i] != 0 and arr[i + 1] != 0:
            res.append(arr[i] * arr[i + 1])
            res.append(arr[i + 1] - 1)
        else:
            res.extend([0, 0])
    if not res:
        print('0 0')
    else:
        print(' '.join(map(str, res)))
