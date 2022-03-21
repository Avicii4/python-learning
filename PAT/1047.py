import re

if __name__ == '__main__':
    n, scores = int(input()), []
    for _ in range(n):
        scores.append(re.split(r'[- ]', input()))
    dct = dict()
    for s in scores:
        dct[s[0]] = dct.get(s[0], 0) + int(s[2])
    x = sorted(dct, key=lambda k: dct[k]).pop()
    print(x, dct[x])
