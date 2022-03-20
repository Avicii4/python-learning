from collections import Counter

if __name__ == '__main__':
    n = int(input())
    scores = map(int, input().split())
    cnt = Counter(scores)
    targets = list(map(int, input().split()))
    res = []
    for i in range(1, len(targets)):
        res.append(str(cnt.get(targets[i], 0)))
    print(' '.join(res))
