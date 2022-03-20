from collections import Counter

if __name__ == '__main__':
    cnt = Counter(''.join(input().lower().split()))
    for i in cnt:
        if i < 'a' or i > 'z':
            cnt.pop(i)
    x = sorted(cnt, key=lambda k: (cnt[k], -ord(k))).pop()
    print(x, cnt[x])
