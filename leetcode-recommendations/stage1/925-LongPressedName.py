class Solution:
    def is_long_presse_name(self, name: str, typed: str) -> bool:
        p = q = 0
        l1, l2 = len(name), len(typed)
        # 先看[p]是否等于[q]，若不等，再看[q]和它前面的是否相同
        # 最后别忘了name是否被全部比较完
        while q < l2:
            if p < l1 and name[p] == typed[q]:
                p += 1
                q += 1
            elif q > 0 and typed[q] == typed[q - 1]:
                q += 1
            else:
                return False
        return p == l1


if __name__ == '__main__':
    sol = Solution()
    n = 'alex'
    t = 'aallex'
    print(sol.is_long_presse_name(n, t))
