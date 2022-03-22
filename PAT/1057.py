if __name__ == '__main__':
    s = input()
    arr = [ch.lower() for ch in s if ch.isalpha()]
    # 不分情况的话，'0'的数量是1个
    if not arr:
        print(0, 0)
    else:
        n = sum([ord(ch) - 96 for ch in arr])
        bin_str = bin(n)[2:]
        cnt = bin_str.count('0')
        print(cnt, len(bin_str) - cnt)
