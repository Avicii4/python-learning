if __name__ == '__main__':
    c1, c2 = map(int, input().split())
    total = (c2 - c1) // 100
    if (c2 - c1) / 100 - total >= 0.5:
        total += 1
    hour = total // 3600
    minute = (total % 3600) // 60
    second = (total % 3600) % 60
    print('{:0>2}:{:0>2}:{:0>2}'.format(hour, minute, second))
