"""
n个小朋友围一圈，小朋友从1~n编号。顺时针方向1 2 3...n
游戏开始从1号开始顺时针报数，每个小朋友报上个小朋友数+1
若一个小朋友的数为k的倍数或其个位数为k，则该小朋友出去，不再参加以后的报数
当游戏中只剩下一个小朋友的时候该小朋友获胜
"""


def game(n: int, k: int) -> int:
    lst = [i + 1 for i in range(n)]
    num = 0  # 当前报的数字
    index = 0  # 当前报数人的下标
    while len(lst) > 1:
        num += 1
        if num % k == 0 or num % 10 == k:
            lst.pop(index)
        else:   # 若有人出队，index不变
            index = (index + 1) % len(lst)
    return lst[0]


if __name__ == '__main__':
    print(game(7, 5))
