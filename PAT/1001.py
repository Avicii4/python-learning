if __name__ == '__main__':
    num, res = int(input()), 0
    while num != 1:
        res += 1
        if num % 2:
            num = (3 * num + 1) // 2
        else:
            num //= 2
    print(res)
