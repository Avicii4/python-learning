# 第一版比较丑
# if __name__ == '__main__':
#     arr = list(map(int, input().split()))[1:]
#     res = []
#
#     arr_1 = [x for x in arr if x % 5 == 0 and x % 2 == 0]
#     if not arr_1:
#         res.append('N')
#     else:
#         res.append(str(sum(arr_1)))
#
#     arr_2 = [x for x in arr if x % 5 == 1]
#     if not arr_2:
#         res.append('N')
#     else:
#         ans = 0
#         for i in range(len(arr_2)):
#             ans += (arr_2[i] * (-1) ** i)
#         res.append(str(ans))
#
#     arr_3 = [x for x in arr if x % 5 == 2]
#     if not arr_3:
#         res.append('N')
#     else:
#         res.append(str(len(arr_3)))
#
#     arr_4 = [x for x in arr if x % 5 == 3]
#     if not arr_4:
#         res.append('N')
#     else:
#         res.append('{:.1f}'.format(sum(arr_4) / len(arr_4)))
#
#     arr_5 = [x for x in arr if x % 5 == 4]
#     if not arr_5:
#         res.append('N')
#     else:
#         res.append(str(max(arr_5)))
#
#     print(' '.join(res))


if __name__ == '__main__':
    arr, res = list(map(int, input().split()))[1:], []
    lsts = []
    for i in range(5):
        lsts.append([x for x in arr if x % 5 == i])
    lsts[0] = [x for x in lsts[0] if x % 2 == 0]
    for i in range(5):
        if not lsts[i]:
            res.append('N')
        elif i == 0:
            res.append(str(sum(lsts[i])))
        elif i == 1:
            ans = 0
            for k in range(len(lsts[i])):
                ans += (lsts[i][k] * (-1) ** k)
            res.append(str(ans))
        elif i == 2:
            res.append(str(len(lsts[i])))
        elif i == 3:
            res.append('{:.1f}'.format(sum(lsts[i]) / len(lsts[i])))
        else:
            res.append(str(max(lsts[i])))
    print(' '.join(res))
