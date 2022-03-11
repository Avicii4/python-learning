def hanoi(n: int, from_stick: str, to_stick: str, help_stick: str):
    if n == 1:
        print('把 {}号盘子 从 {} 移动到 {} 上'.format(1, from_stick, to_stick))
    else:
        hanoi(n - 1, from_stick, help_stick, to_stick)
        print('把 {}号盘子 从 {} 移动到 {} 上'.format(n, from_stick, to_stick))
        hanoi(n - 1, help_stick, to_stick, from_stick)


if __name__ == '__main__':
    # 把所有盘子从左柱子移到右柱子上
    n = 3
    f, t, h = '左柱子', '右柱子', '中柱子'
    hanoi(n, f, t, h)
