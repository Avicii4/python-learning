from random import randint


def find_common_keys(dct_1: dict, dct_2: dict) -> list:
    return [k1 for k1 in dct_1.keys() for k2 in dct_2.keys() if k1 == k2]


if __name__ == '__main__':
    d1 = {}
    d2 = {}
    for i in range(50):
        r1 = randint(0, 100)
        r2 = randint(0, 100)
        d1[r1] = d1.get(r1, 0) + 1
        d2[r2] = d2.get(r2, 0) + 1
    print('字典一：{}'.format(d1))
    print('字典二：{}'.format(d2))
    print(find_common_keys(d1, d2))
