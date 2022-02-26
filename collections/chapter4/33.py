def sum_index(num: int) -> int:
    lst = [n for n in range(2, num) if num % n == 0]
    return sum(lst)


if __name__ == '__main__':
    while True:
        n = int(input('请输入一个整数：'))
        if n == 0:
            exit()
        print(sum_index(abs(n)))
