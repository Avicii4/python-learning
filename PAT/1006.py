if __name__ == '__main__':
    numbers = '123456789'
    n = input()
    base = numbers[:int(n[-1])]
    if len(n) == 1:
        print(base)
    elif len(n) == 2:
        print('S' * int(n[0]) + base)
    else:
        print('B' * int(n[0]) + 'S' * int(n[1]) + base)
