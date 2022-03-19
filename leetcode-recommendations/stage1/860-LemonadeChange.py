from typing import List


class Solution:
    # 此法涉及到wallet[]的多次遍历寻找，耗时大
    def lemonade_change_1(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False
        wallet = []
        for bill in bills:
            wallet.append(bill)
            if bill == 10:
                if 5 not in wallet:
                    return False
                else:
                    wallet.remove(5)
            elif bill == 20:
                if 10 in wallet and 5 in wallet:
                    wallet.remove(5)
                    wallet.remove(10)
                elif wallet.count(5) >= 3:
                    for _ in range(3):
                        wallet.remove(5)
                else:
                    return False
        return True

    # 找零只涉及5美元和10美元
    def lemonade_change_2(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five < 1:
                    return False
                else:
                    five -= 1
                    ten += 1
            else:
                # 5美元比较珍贵，优先找出10美元面额
                if five >= 1 and ten >= 1:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


if __name__ == '__main__':
    sol = Solution()
    while True:
        bills = list(map(int, input('请输入支付金额：').split()))
        if not bills:
            exit(-1)
        print(sol.lemonade_change_2(bills))
