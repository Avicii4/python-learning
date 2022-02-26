"""
假设有一段英文，其中有单独的字母I误写为了i，请编写程序纠正
"""

if __name__ == '__main__':
    s = 'i am a girl.'
    s = s.replace('i ', 'I ')
    s = s.replace(' i ', ' I ')
    print(s)
