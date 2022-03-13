if __name__ == '__main__':
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(input().split())
    lst.sort(key=lambda x: int(x[2]))
    print(lst[-1][0], lst[-1][1])
    print(lst[0][0], lst[-0][1])
