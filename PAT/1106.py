if __name__ == '__main__':
    n, lst = int(input()), [2, 0, 1, 9]
    for i in range(n - 4):
        s = str(lst[i] + lst[i + 1] + lst[i + 2] + lst[i + 3])
        lst.append(int(s[-1]))
    # 注意n可能小于4
    print(''.join(map(str, lst[:n])))
