from functools import reduce


class Solution:
    def subtract_product_and_sum(self, n: int) -> int:
        lst = list(map(int, list(str(n))))
        product = reduce(lambda x, y: x * y, lst)
        return product - sum(lst)

    def xiu(self, n: int) -> int:
        return eval('*'.join(list(str(n)))) - eval('+'.join(list(str(n))))


if __name__ == '__main__':
    sol = Solution()
    print(sol.xiu(1234))
