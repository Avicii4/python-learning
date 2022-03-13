if __name__ == '__main__':
    words = ('ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu')
    n = input()
    sum = eval('+'.join(list(n)))
    print(' '.join([words[int(i)] for i in str(sum)]))
