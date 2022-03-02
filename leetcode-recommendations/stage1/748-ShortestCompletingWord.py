from typing import List
from collections import Counter


class Solution:
    # 原来就是词频统计，直接用Counter
    def shortest_completing_word_1(self, license_plate: str, words: List[str]) -> str:
        cnt = Counter(ch.lower() for ch in license_plate if ch.isalpha())
        # 若 not cnt - Counter(word)，说明word包含全部cnt的字母
        return min((word for word in words if not cnt - Counter(word)), key=len)

    def shortest_completing_word_2(self, license_plate: str, words: List[str]) -> str:
        lst = [i.lower() for i in license_plate if i.isalpha()]
        words.sort(key=len)
        # 和words里的一个个word比
        for word in words:
            l = lst[:]
            for ch in word:
                # 若word中的字母也在 license_plate里，则从license_plate移除
                if ch in l:
                    l.remove(ch)
                # l为空，说明license_plate里有的字母，word都有
                if not l:
                    return word


if __name__ == '__main__':
    sol = Solution()
    while True:
        plate = input('请输入字符串：')
        if not plate:
            exit(-1)
        ws = input('请输入字符串数组：').split()
        print(sol.shortest_completing_word_2(plate, ws))
