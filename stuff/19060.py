def test(lst):
    return sum(not n % 2 for n in lst)


if __name__ == '__main__':
    print(test([]))
    print(test([13, 11, 5, -9]))
