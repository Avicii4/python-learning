"""
A队长说：不是我们队，也不是C队
B队长说：是我们队或者D队
C队长说：是A队，不是B队
D队长说：B队长说错了
学长说：四个队长只有一个是真话，请问哪支队伍赢了比赛？
"""
# 答：C队

if __name__ == '__main__':
    teams = 'ABCD'
    for ch in teams:
        counter = 0  # 计算真话数量
        if ch != 'A' and ch != 'C':
            counter += 1
        if ch == 'B' or ch == 'D':
            counter += 1
        if ch == 'A':
            counter += 1
        if ch != 'B' and ch != 'D':
            counter += 1
        if counter == 1:
            print('获胜者是{}队'.format(ch))
            break

