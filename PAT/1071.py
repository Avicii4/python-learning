if __name__ == '__main__':
    token, k = map(int, input().split())
    game = []
    for _ in range(k):
        # 一定要这样写，否则测试点4不通过
        g = list(map(int, input().split()))
        if token <= 0:
            print('Game Over.')
            break
        elif g[2] > token:
            print('Not enough tokens.  Total = {}.'.format(token))
        else:
            if (g[0] > g[-1] and g[1] == 0) or (g[0] < g[-1] and g[1] == 1):
                token += g[2]
                print('Win {}!  Total = {}.'.format(g[2], token))
            else:
                token -= g[2]
                print('Lose {}.  Total = {}.'.format(g[2], token))
                if token <= 0:
                    print('Game Over.')
                    break
