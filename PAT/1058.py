import re

if __name__ == '__main__':
    n, m = map(int, input().split())
    question_lst, answer_lst = [], []
    for _ in range(m):
        question_lst.append(input().split())
    score, err_cnt = [0] * n, [0] * m
    for st in range(n):
        # TODO 去头去尾再划分，避免s中有空元素
        s = re.split(r'[( )]+', input()[1:-1])
        seq = 0
        for i in range(len(s)):
            if s[i].isdigit():
                tmp = s[i + 1:i + 1 + int(s[i])]
                if tmp == question_lst[seq][3:]:
                    score[st] += int(question_lst[seq][0])
                else:
                    err_cnt[seq] += 1
                seq += 1
    for i in score:
        print(i)
    if sum(err_cnt) == 0:
        print('Too simple')
    else:
        res = [max(err_cnt)]
        for k in range(m):
            if err_cnt[k] == res[0]:
                res.append(k + 1)
        print(' '.join(map(str, res)))
