# 超时，但代码还行
if __name__ == '__main__':
    n, l, h = map(int, input().split())
    scores = []
    for i in range(n):
        scores.append(list(map(int, input().split())))
    scores = [score for score in scores if score[1] >= l and score[2] >= l]
    c = [[s for s in scores if s[1] >= h and s[2] >= h],
         [s for s in scores if s[1] >= h > s[2]],
         [s for s in scores if h > s[1] >= s[2] and s[2] < h],
         [s for s in scores if s[1] < h and s[1] < s[2]]]
    for i in range(4):
        c[i].sort(key=lambda x: (-x[1] - x[2], -x[1], x[0]))
    c = [m for item in c for m in item]
    print(len(c))
    for o, p, q in c:
        print(o, p, q)
