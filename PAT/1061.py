if __name__ == '__main__':
    n, m = map(int, input().split())
    marks = list(map(int, input().split()))
    correct_ans = list(map(int, input().split()))
    res = [0] * n
    for i in range(n):
        p = list(map(int, input().split()))
        for j in range(m):
            if p[j] == correct_ans[j]:
                res[i] += marks[j]
    for n in res:
        print(n)
