if __name__ == '__main__':
    d, n = input().split()
    res = d
    for _ in range(int(n) - 1):
        i, tmp, cnt = 0, '', 1
        while i < len(res):
            if i == len(res) - 1:
                tmp += res[i] + str(cnt)
            elif res[i] == res[i + 1]:
                cnt += 1
            else:
                tmp += res[i] + str(cnt)
                cnt = 1
            i += 1
        else:
            res = tmp
    print(res)
