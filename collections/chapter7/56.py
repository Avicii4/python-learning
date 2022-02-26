def merge():
    names = ['files/folder/file' + str(i) + '.txt' for i in range(1, 5)]
    with open('files/folder/merge.txt', 'w', encoding='utf-8') as f:
        for name in names:
            with open(name, 'r', encoding='utf-8') as ff:
                s = ff.read()
                f.write(s)


if __name__ == '__main__':
    merge()
