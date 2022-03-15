import re
import random


def is_prime(n: int) -> bool:
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


if __name__ == '__main__':
    content = "Regular296expression913patterns465are280compiled102into510a122series48" \
              "of563bytecodes16which366are262then773executed361by50a949matching556eng" \
              "ine509written126in451C760For379advanced982use201it502may282be666necess" \
              "ary566to631pay199careful685attention915to814how577the455engine309will3" \
              "49execute178a341given171RE279and52write744the69RE578in190a361certain46" \
              "6way726in969order667to310produce943bytecode760that203runs590faster4230" \
              "ptimization723is787not458covered30in250this747document66because396it80" \
              "3requires530that601you928have208a152good609understanding194of31the772m" \
              "atching17engine599internals806"
    pattern = re.compile(r'\d+')
    nums = pattern.findall(content)
    nums = [n for n in nums if is_prime(int(n)) and ('3' in n or '7' in n)]
    flag = 0
    for n in nums:
        print('{}'.format(n).rjust(10), end='')
        flag += 1
        if not flag % 2:
            print()

    x, y = random.uniform(0, 100), random.uniform(0, 100)
    print('\n(' + '{:.2f}'.format(x).rjust(10) + ',' + '{:.2f}'.format(y).rjust(10) + ')')

    dis_sum = 0
    nums = list(map(int, nums))
    if len(nums) % 2:
        nums = nums[:-1]
    for i in range(0, len(nums), 2):
        dis_sum += ((nums[i] - x) ** 2 + (nums[i + 1] - y) ** 2) ** 0.5
    print('距离之和为：{:.2f}'.format(dis_sum).rjust(10))
    print('平均距离为：{:.2f}'.format(dis_sum / (len(nums) // 2)).rjust(10))

    pattern = re.compile(r'[a-zA-Z]+')
    words = pattern.findall(content)
    print('单词ASCII之和：')
    index = []
    for word in words:
        index.append(sum([ord(ch) for ch in word]))
    flag = 0
    for i in index:
        print('{}'.format(i).ljust(8), end='')
        flag += 1
        if not flag % 10:
            print()
