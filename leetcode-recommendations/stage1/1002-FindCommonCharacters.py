from typing import List
from collections import Counter


class Solution:
    # 朴实的Counter用法
    def common_chars_1(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return list(words[0])
        counter_list, res = [], []
        for word in words:
            counter_list.append(Counter(word))
        for ch in counter_list[0]:
            ch_min = counter_list[0][ch]
            for i in range(1, len(counter_list)):
                if ch not in counter_list[i]:
                    break
                elif counter_list[i][ch] < ch_min:
                    ch_min = counter_list[i][ch]
            else:
                for i in range(ch_min):
                    res.append(ch)
        return res

    # 顶级Counter用法 交集
    def common_chars_2(self, words: List[str]) -> List[str]:
        res = None
        for word in words:
            cnt = Counter(word)
            if res is None:
                res = cnt
            else:
                res &= cnt
        # TODO 按字典中的数量输出
        return list(res.elements())


if __name__ == '__main__':
    sol = Solution()
    arr = ["cool", "lock", "cook"]
    print(sol.common_chars_2(arr))
