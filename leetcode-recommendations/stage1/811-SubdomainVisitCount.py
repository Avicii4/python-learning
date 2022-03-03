from typing import List


class Solution:
    # 题目明确cpdomain[i] 会遵循 "repi d1i.d2i.d3i" 或 "repi d1i.d2i" 格式
    # 故代码可比较复杂，但省时间
    def subdomain_visits(self, cpdomains: List[str]) -> List[str]:
        dct = {}
        for elem in cpdomains:
            elems = elem.split()
            total = int(elems[0])
            domain_lst = elems[1].split('.')
            dct[domain_lst[-1]] = dct.get(domain_lst[-1], 0) + total
            r = domain_lst[-2] + '.' + domain_lst[-1]
            dct[r] = dct.get(r, 0) + total
            if len(domain_lst) == 3:
                dct[elems[1]] = dct.get(elems[1], 0) + total
        # 以下写法麻烦 但耗时短
        # res = []
        # for item in dct.items():
        #     st = str(item[1]) + ' ' + item[0]
        #     res.append(st)
        # return res
        return ['{} {}'.format(v, i) for i, v in dct.items()]


if __name__ == '__main__':
    sol = Solution()
    cps = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    print(sol.subdomain_visits(cps))
