# 素数老问题，超时
if __name__ == '__main__':
    m, n = map(int, input().split())
    # cnt记录是第几个素数,flag记录换行
    cnt, flag, num = 0, 0, 2
    while cnt < n:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            cnt += 1
            if cnt >= m:
                flag += 1
                print(num, end='')
                if not flag % 10:
                    print()
                # 最后一个数之后也不能有空格
                elif cnt != n:
                    print(' ', end='')
        num += 1
