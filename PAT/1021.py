from collections import Counter

if __name__ == '__main__':
    cnt = Counter(input())
    for k in sorted(cnt):
        print('{}:{}'.format(k, cnt[k]))
