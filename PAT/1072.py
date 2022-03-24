if __name__ == '__main__':
    n, m = map(int, input().split())
    target = input().split()
    record, cnt = [], 0
    for _ in range(n):
        arr = input().split()
        tmp = [arr[0]]
        for i in arr[2:]:
            if i in target:
                tmp.append(i)
                cnt += 1
        else:
            if len(tmp) > 1:
                record.append(tmp)
    for r in record:
        print('{}: {}'.format(r[0], ' '.join(r[1:])))
    print(len(record), cnt)
