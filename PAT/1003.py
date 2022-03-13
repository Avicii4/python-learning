"""
此题没做出来，其主要约束是：
以字符P，T进行分段，P前段为a，P T之间为b，T之后为c，
则若它是正确答案，有c=a*len(b)
"""
import re

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        s = input()
        # 注意'P'和'T'之间至少有一个'A'
        if re.match(r'A*PA+TA*', s):
            # 以'P'或者'T'进行划分
            arr = re.split(r'[P|T]', s)
            if arr[2] == arr[0] * len(arr[1]):
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
