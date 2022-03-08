from typing import List


class Solution:
    def is_alien_sorted_1(self, words: List[str], order: str) -> bool:
        order_words = list(sorted(words, key=lambda x: [order.index(ch) for ch in x]))
        return order_words == words

    def is_alien_sorted_2(self, words: List[str], order: str) -> bool:
        order_map = {v: i for i, v in enumerate(order)}
        return words == list(sorted(words, key=lambda x: [order_map[ch] for ch in x]))

    # 依次比较相邻单词
    def is_alien_sorted_3(self, words: List[str], order: str) -> bool:
        order_map = {v: i for i, v in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            for k in range(min(len(w1), len(w2))):
                if w1[k] != w2[k]:
                    if order_map[w1[k]] > order_map[w2[k]]:
                        return False
                    # 第一个不同的字母顺序正确，剩下字母的不用比较
                    break
            else:
                if len(w1) > len(w2):
                    return False

        return True


if __name__ == '__main__':
    sol = Solution()
    words = ['zoos', 'zoo', "able", "hello", "leetcode"]
    order = 'hlabcdefgijkmnopqrstuvwxyz'
    print(sol.is_alien_sorted_2(words, order))
