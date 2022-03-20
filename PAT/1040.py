# res = 0
#
#
# # 无脑暴力递归，两用例超时
# def find(s: str, index: int, pos: int):
#     global res
#     if index == len(s):
#         return
#     if pos == 0:
#         for i in range(index, len(s) - 2):
#             if s[i] == 'P':
#                 find(s, i + 1, pos + 1)
#     elif pos == 1:
#         for i in range(index, len(s) - 1):
#             if s[i] == 'A':
#                 find(s, i + 1, pos + 1)
#     else:
#         for i in range(index, len(s)):
#             if s[i] == 'T':
#                 res += 1
#
#
# if __name__ == '__main__':
#     s = input().lstrip('AT')
#     s = s.rstrip('PA')
#     find(s, 0, 0)
#     print(res % 1000000007)

# 对s中每一个'A'，前面'P'的个数乘后面'T'的个数
if __name__ == '__main__':
    s = input().lstrip('AT')
    s = s.rstrip('PA')
    res = cnt_p = 0
    cnt_t = s.count('T')
    for ch in s:
        if ch == 'A':
            res += (cnt_t * cnt_p)
        elif ch == 'P':
            cnt_p += 1
        else:
            cnt_t -= 1
    print(res % 1000000007)
