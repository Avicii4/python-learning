from collections import Counter

if __name__ == '__main__':
    sell = Counter(input())
    want = Counter(input())
    delta = want - sell
    if not delta:
        print('{} {}'.format('Yes', sum((sell-want).values())))
    else:
        print('{} {}'.format('No', sum(delta.values())))
