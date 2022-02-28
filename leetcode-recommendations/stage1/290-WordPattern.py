class Solution:
    def word_pattern(self, pattern: str, s: str) -> bool:
        """
        基本思想是用字典记录pattern的字母与单词的对应关系
        有两种情况，函数要返回False：
        情况一：当前pattern的字母在字典中已有记录，但与现在s_list中的单词不匹配
        情况二：现在检验的s_list中的单词已存在字典中，但其key与当前pattern中的字母不同
        可以发现情况一好处理，而情况二要根据value取key值，不好处理
        有没有除了创建两个字典外的方法？有的
        若出现了情况二，则len(set(s_list))和len(set(pattern))必定不会相等
        且前者肯定小于后者，据此可得答案
        """
        s_list = s.split()
        if len(s_list) != len(pattern):
            return False
        # 针对情况二
        if len(set(s_list)) != len(set(pattern)):
            return False
        dct = {}
        for i in range(len(pattern)):
            if pattern[i] not in dct.keys() and s_list[i] not in dct.values():
                dct[pattern[i]] = s_list[i]
            elif pattern[i] in dct.keys() and dct[pattern[i]] != s_list[i]:
                # 对应情况一
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    while True:
        pt = input('请输入模式串：')
        s = input('请输入单词列表：')
        print(sol.word_pattern(pt, s))
