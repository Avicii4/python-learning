import string

n = 5
l = string.ascii_lowercase
u = string.ascii_uppercase


def encrypt(s):
    res = ''
    for ch in s:
        if 'a' <= ch <= 'z':
            res += l[(l.find(ch) + n) % 26]
        elif 'A' <= ch <= 'Z':
            res += u[(u.find(ch) + n) % 26]
        else:
            res += ch
    return res


def decrypt(s):
    res = ''
    for ch in s:
        if 'a' <= ch <= 'z':
            res += l[(l.find(ch) + 26 - n) % 26]
        elif 'A' <= ch <= 'Z':
            res += u[(u.find(ch) + 26 - n) % 26]
        else:
            res += ch
    return res


if __name__ == '__main__':
    while True:
        origin = input('请输入待加密字符串：')
        if origin == '':
            exit('用户主动中止')
        en_str = encrypt(origin)
        de_str = decrypt(en_str)
        print('加密后：{}'.format(en_str))
        print('解密后：{}'.format(de_str))
