"""
读取 2008_in.txt 中所有的英文单词（大小写敏感），其中有若干长度小于 15 的英文单词；
读取时排除所有单词'The'及其变型；将所有单词首字母大写以后输出到 2008_out.txt 中
"""
import re

if __name__ == '__main__':
    with open('file/2008_in.txt', 'rt', encoding='utf-8') as f1:
        content = f1.read()
    pat = re.compile(r'[a-zA-z]+')
    lst = set(re.findall(pat, content))
    res = [s.capitalize() for s in lst if s.upper() != 'THE']
    with open('file/2008_out.txt', 'w', encoding='utf-8') as f2:
        for w in set(res):
            f2.write(w + '\n')
