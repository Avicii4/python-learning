from typing import List


class Solution:
    # 直接法
    def unique_morse_representations_1(self, words: List[str]) -> int:
        table = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                 "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                 "...-", ".--", "-..-", "-.--", "--.."]
        morses = []
        for word in words:
            s = str()
            for ch in word:
                s += table[ord(ch) - 97]
            morses.append(s)
        return len(set(morses))

    # 和上面主要的区别是，一开始就是往集合里加，而非之后再转成集合
    def unique_morse_representations_2(self, words: List[str]) -> int:
        table = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                 "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                 "...-", ".--", "-..-", "-.--", "--.."]
        morses = {''.join(table[ord(i) - 97] for i in word) for word in words}
        return len(morses)


if __name__ == '__main__':
    sol = Solution()
    while True:
        words = input('请输入单词列表：').split()
        if not words:
            exit(-1)
        print(sol.unique_morse_representations_2(words))
