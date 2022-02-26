"""
有一段英文中单词重复了两次，检查并去重
"""
import re

if __name__ == '__main__':
    s = 'This is is a a desk.'
    pattern = r'\b(\w+)\s+\1\b'
    print(re.sub(pattern, r'\1', s))
