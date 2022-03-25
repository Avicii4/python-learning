if __name__ == '__main__':
    a = input()
    b = input()
    # 数组长度如果写126不够
    lst = [0] * 200
    for ch in a + b:
        if lst[ord(ch)] == 0:
            print(ch, end='')
            lst[ord(ch)] += 1
