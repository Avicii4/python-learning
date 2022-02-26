def copy(origin, new):
    with open(origin, 'r', encoding='utf-8') as f1:
        s = f1.read()
    with open(new, 'w', encoding='utf-8') as f2:
        f2.write(s)


if __name__ == '__main__':
    a = 'files/copy.txt'
    b = 'files/new.txt'
    copy(a, b)
