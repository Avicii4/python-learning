"""
Base64编码本质上是3字节转成4组，每组6bit
"""
import string as ss
import base64


# 自己实现
def base64_encode(s):
    old_bin = result = ''
    temp_str = []
    base64_list = ss.ascii_uppercase + ss.ascii_lowercase + ss.digits + '+/'
    for ch in s:
        temp = int(bin(ord(ch)).replace('0b', ''))
        old_bin += '{:08}'.format(temp)  # 长度必须为8，不足补零

    for i in range(0, len(old_bin), 6):
        temp_str.append('{:<06}'.format(old_bin[i:i + 6]))  # 左对齐长6

    for item in temp_str:
        result += base64_list[int(item, 2)]
    if len(result) % 4 == 2:
        result += '=='
    elif len(result) % 4 == 3:
        result += '='
    return result


if __name__ == '__main__':
    # while True:
    #     print(base64_encode(input('要编码内容：')))
    res = base64.b64encode('哈哈哈！'.encode('utf-8'))
    print(str(res, 'utf-8'))
    res = base64.b64encode('哈哈哈！'.encode('gbk'))
    print(str(res, 'gbk'))
