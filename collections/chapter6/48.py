def calc(data: tuple) -> float:
    avg = sum(data) / len(data)
    var = sum([(num - avg) ** 2 for num in data]) / len(data)
    return var


if __name__ == '__main__':
    datas = (65.5, 70.2, 100.5, 45.5, 88.8, 55.5, 73.5, 67.8)
    print(calc(datas))
