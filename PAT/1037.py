if __name__ == '__main__':
    p, a = input().split()
    p = list(map(int, p.split('.')))
    a = list(map(int, a.split('.')))
    sum_p = 17 * 29 * p[0] + 29 * p[1] + p[2]
    sum_a = 17 * 29 * a[0] + 29 * a[1] + a[2]
    if sum_a - sum_p < 0:
        flag = -1
    else:
        flag = 1
    total = abs(sum_a - sum_p)
    k = total % 29
    s = (total // 29) % 17
    g = total // (29 * 17)
    print('{}.{}.{}'.format(flag * g, s, k))

# import re
#
#
# def To_Knut(a1, a2, a3):
#     return a1 * 17 * 29 + a2 * 29 + a3
#
#
# # 将纳特转换为正常的形式
# def To_normal_form(n):
#     # 钱不够，输出字符串也要加负号
#     if n < 0:
#         symbol = '-'
#         n = abs(n)
#     else:
#         symbol = ''
#     galleon = n // (17 * 29)
#     sickle = (n - galleon * 17 * 29) // 29
#     knut = n % 29
#     return symbol + '.'.join(list(map(str, [galleon, sickle, knut])))
#
#
# a1, a2, a3, b1, b2, b3 = map(int, re.split('[. ]', input()))
#
# small_change = To_Knut(b1, b2, b3) - To_Knut(a1, a2, a3)
#
# print(To_normal_form(small_change))
