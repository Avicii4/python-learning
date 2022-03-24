if __name__ == '__main__':
    n, m = map(int, input().split())
    scores = []
    for _ in range(n):
        s = list(map(int, input().split()))
        lst = [num for num in s if 0 <= num <= m]
        arr = lst[1:]
        arr.remove(max(arr))
        arr.remove(min(arr))
        res = (lst[0] + (sum(arr) / len(arr))) / 2
        if res - int(res) >= 0.5:
            scores.append(int(res) + 1)
        else:
            scores.append(int(res))
    for k in scores:
        print(k)
