if __name__ == '__main__':
    # 库存、价格等可能是小数，输入应使用eval
    n, demand = map(int, input().split())
    storage = list(map(int, input().split()))
    price = list(map(int, input().split()))
    rate = [price[k] / storage[k] for k in range(n)]
    ranking = [rate.index(r) for r in sorted(rate, reverse=True)]
    profit = i = 0
    while demand > 0:
        # 总库存不满足需求
        if i == n:
            break
        idx = ranking[i]
        # 库存全部售出
        if demand >= storage[idx]:
            profit += price[idx]
            i += 1
            demand -= storage[idx]
        # 库存部分售出
        else:
            profit += price[idx] * demand / (storage[idx])
            break
    print('{:.2f}'.format(profit))
