from math import sqrt

if __name__ == '__main__':
    lst = [num for num in range(2, 500) if 0 not in [num % n for n in range(2, int(sqrt(num)) + 1)]]
    i = 0
    for v in lst:
        print(v, end='\t')
        i += 1
        if i % 5 == 0:
            print()
