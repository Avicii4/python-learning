"""
该加密算法的密钥是一系列字母，比如一个英文单词PIZZA
• 该单词密钥会分成若干个子密钥
• 第1个子密钥是P，加密明文的第1个字母
• 第2个子密钥是I，加密明文的第2个字母，其余如此类推
• 加密明文的第6个字母，则回过头来使用第1个子密钥P
"""
import string

LETTERS = string.ascii_uppercase


def translate_msg(msg, key, mode):
    cipher = []  # 加密解密结果
    key = key.upper()
    key_index = 0  # 当前使用密钥字母索引
    for ch in msg:
        index = LETTERS.find(ch.upper())
        if index != -1:
            if mode == 'encrypt':
                index += LETTERS.find(key[key_index])
            elif mode == 'decrypt':
                index -= LETTERS.find(key[key_index])
            index %= len(LETTERS)
            if ch.isupper():
                cipher.append(LETTERS[index])
            else:
                cipher.append(LETTERS[index].lower())
            key_index = (key_index + 1) % len(key)
        else:
            cipher.append(ch)  # 非字母不进行加密
    return ''.join(cipher)


def encrypt(msg, key):
    return translate_msg(msg, key, 'encrypt')


def decrypt(msg, key):
    return translate_msg(msg, key, 'decrypt')


if __name__ == '__main__':
    origin = 'The Vigenère cipher is a method of encrypting alphabetic ' \
             'text by using a series of interwoven Caesar ciphers, based ' \
             'on the letters of a keyword.'
    ckey = 'OLYMPICS'
    print('加密前：' + origin)
    p = encrypt(origin, ckey)
    print('加密后：' + p)
    print('解密后：' + decrypt(p, ckey))
