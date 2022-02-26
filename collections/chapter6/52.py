from random import randint


def generate_sets():
    set_1 = set()
    set_2 = set()
    while len(set_1) < 200:
        set_1.add(randint(0, 501))
    while len(set_2) < 200:
        set_2.add(randint(0, 501))

    print('Non-shared data:')
    s1 = set_1 ^ set_2  # 对称差
    i = 0
    for num in s1:
        print('{}'.format(num).rjust(5), end='')
        i += 1
        if i % 10 == 0:
            print()
    print('\nShared data:')
    s2 = set_1 & set_2  # 交集
    i = 0
    for num in s2:
        print('{}'.format(num).rjust(5), end='')
        i += 1
        if i % 10 == 0:
            print()


if __name__ == '__main__':
    generate_sets()
