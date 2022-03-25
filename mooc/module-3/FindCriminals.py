"""
有5个抢劫案嫌疑人分别是A、B、C、D和E
已知有以下条件：
1. 如果A参与了犯罪,则B一定也参与了
2. B和C只有一个人参与了犯罪
3. C和D要么都参加，要么都没参加
4. D和E至少有一个人参加犯罪
5. 如果E作案，那么A和D一定参与作案
请找出哪些人是真正的罪犯
"""

if __name__ == '__main__':
    values = (0, 1)  # 0未参加  1参加
    arr = ('A', 'B', 'C', 'D', 'E')
    candidates = [(A, B, C, D, E)
                  for A in values
                  for B in values
                  for C in values
                  for D in values
                  for E in values]   # 创造幂集，值得学习
    for item in candidates:
        count = 0  # 计算满足五个条件的多少
        if item[0] + item[1] == 2 or item[0] == 0:  # A、B都参加或A没参加
            count += 1
        if item[1] + item[2] == 1:  # B，C一人参加
            count += 1
        if item[2] == item[3]:  # C、D共进退
            count += 1
        if item[3] + item[4] >= 1:  # D、E至少一人参加
            count += 1
        if item[0] + item[3] + item[4] == 3 or item[4] == 0:  # E、A、D一起参加或E没参加
            count += 1
        if count == 5:
            print('罪犯是' + '、'.join(arr[i] for i in range(5) if item[i] == 1))
            break
