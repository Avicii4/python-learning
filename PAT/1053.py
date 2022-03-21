if __name__ == '__main__':
    n, e, d = map(float, input().split())
    record = []
    for _ in range(int(n)):
        record.append(tuple(map(float, input().split()[1:])))
    may_empty = empty = 0
    for u in record:
        low = [n for n in u if n < e]
        if len(low) >= len(u) // 2 + 1:
            may_empty += 1
            if len(u) > d:
                may_empty -= 1
                empty += 1
    print('{:.1f}% {:.1f}%'.format(100 * (may_empty / n), 100 * (empty / n)))
