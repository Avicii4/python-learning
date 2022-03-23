"""
这题没做出来，有几点注意：
1. 所有提供的绳子都要使用到
2. 'cur = (cur + ropes[i]) // 2' 写法正确；'cur = cur // 2 + ropes[i] // 2' 写法错误
3. 一开始加入的绳子在之后要经历数次对折，长的绳子每次对折损失的长度较大，因而要先加入短绳子，
   降低每次的损耗
"""
if __name__ == '__main__':
    n = int(input())
    ropes = list(map(int, input().split()))
    ropes.sort()
    cur = mmax = ropes[0]
    for i in range(1, n):
        cur = (cur + ropes[i]) // 2
        cur = cur // 2 + ropes[i] // 2
        if cur > mmax:
            mmax = cur
    print(mmax)
