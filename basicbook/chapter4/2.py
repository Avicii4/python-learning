"""
假设有一段英文，其中有单词中间的字母i误写为I，请编写程序进行纠正
"""
import re

if __name__ == '__main__':
    s = 'I am a gIrl.'
    pattern = r'\BI\B'
    print(re.sub(pattern, 'i', s))
