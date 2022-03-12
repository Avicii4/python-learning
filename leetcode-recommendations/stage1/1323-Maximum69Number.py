class Solution:
    # 转成数组再遍历
    def maximum_number_1(self, num: int) -> int:
        lst = list(str(num))
        for i in range(len(lst)):
            if lst[i] == '6':
                lst[i] = '9'
                break
        return int(''.join(lst))

    # 字符串替换，最多换一个
    def maximum_number_2(self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximum_number_2(69969))
