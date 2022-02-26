def employees():
    dct = {}
    num = int(input('Please input the number of employees:'))
    if num == 0:
        exit('用户主动中止')
    for i in range(num):
        name = input('Name of employee No.{}:'.format(i + 1))
        seq = int(input('Serial number of employee No.{}:'.format(i + 1)))
        dct[name] = seq

    print('Sorted by names:')
    for i in sorted(dct):
        print('{}:{}'.format(i, dct[i]), end=' ')
    print('\nSorted by serial numbers:')
    for i in sorted(dct, key=lambda x: dct[x]):  # dct默认是所有的key集合，x就是集合中的每一个key，排序的依据是dct[x]，即每个value
        print('{}:{}'.format(dct[i], i), end=' ')


if __name__ == '__main__':
    employees()
