"""
利用dict.txt实现查字典
"""


def search(file_name, word):
    with open(file_name, 'rt', encoding='utf-8') as file:
        res = []
        line = file.readline()
        while line != '':
            index = line.find('[解释]')
            if index == -1:
                continue
            else:
                if word in line[:index - 1]:  # 模糊查询
                    res.append(line.strip())
            line = file.readline()
    return res


if __name__ == '__main__':
    while True:
        w = input('请输入查找单词：')
        s = search('files/dict.txt', w)
        if len(s) == 0:
            print('无查找结果')
        else:
            for i in s:
                print(i)

