if __name__ == '__main__':
    """
    这个做法错误，无法解决如：
    This
    Thi
    这样的问题
    """
    # complete = input().upper()
    # incomplete = input().upper()
    # res = []
    # i = j = 0
    # while i < len(complete) and j < len(incomplete):
    #     if complete[i] != incomplete[j]:
    #         if complete[i] not in res:
    #             res.append(complete[i])
    #     else:
    #         j += 1
    #     i += 1
    # print(''.join(res))

    complete = list(input().upper())
    incomplete = list(input().upper())
    lst = [x for x in complete if x not in incomplete]
    res = list(set(lst))
    res.sort(key=lst.index)
    print(''.join(res))



