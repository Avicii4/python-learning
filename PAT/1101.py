if __name__ == '__main__':
    a, d = input().split()
    n, d = len(a), int(d)
    b = int(a[n - d:] + a[:n - d])
    print('{:.2f}'.format(b / int(a)))
