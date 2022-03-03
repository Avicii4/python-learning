class Solution:
    def to_goat_latin(self, sentence: str) -> str:
        vowels = tuple('aeiouAEIOU')
        words = sentence.split()
        res = []
        for i, word in enumerate(words):
            if word[0] in vowels:
                res.append(word + 'ma' + 'a' * (i + 1))
            else:
                res.append(word[1:] + word[0] + 'ma' + 'a' * (i + 1))
        return ' '.join(res)


if __name__ == '__main__':
    sol = Solution()
    while True:
        x = input('请输入一个句子：')
        if not x:
            exit(-1)
        print(sol.to_goat_latin(x))
