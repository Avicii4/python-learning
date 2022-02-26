from random import randint


def test():
    A = set()
    B = set()
    len_a = randint(1, 6)
    len_b = randint(1, 6)
    while len(A) < len_a:
        A.add(randint(0, 10))
    while len(B) < len_b:
        B.add(randint(0, 10))
    print('A = {}'.format(A))
    print('B = {}'.format(B))
    union = A | B
    intersection = A & B
    chance = 3
    while chance > 0:
        a = map(int, input('A|B = ').split())
        b = map(int, input('A&B = ').split())
        if set(a) == union and set(b) == intersection:
            return 'Correct answer!'
        else:
            chance -= 1
            print('Wrong answer, {} chance(s) left.'.format(chance))
    if not union:
        union = 'null'
    if not intersection:
        intersection = 'null'
    return 'The answer is:\nA|B = {},\nA&B = {}'.format(union, intersection)


if __name__ == '__main__':
    print(test())
