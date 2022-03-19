if __name__ == '__main__':
    col, sign = input().split()
    col = int(col)
    row = col // 2 if not col % 2 else col // 2 + 1
    print(sign * col)
    for i in range(row - 2):
        print(sign + ' ' * (col - 2) + sign)
    print(sign * col)
