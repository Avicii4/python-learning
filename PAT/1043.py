if __name__ == '__main__':
    s, res = list(input()), []
    m = 'PATest'
    s = [ch for ch in s if ch in m]
    while s:
        for ch in m:
            if ch in s:
                res.append(ch)
                s.remove(ch)
    print(''.join(res))
