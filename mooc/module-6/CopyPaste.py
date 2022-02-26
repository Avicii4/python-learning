"""
编写程序将cat2的内容复制到cat1文件的最后面
"""


def paste(file_1, file_2):
    with open(file_2, 'r', encoding='utf-8') as f2:
        s = f2.read()
    with open(file_1, 'a+', encoding='utf-8') as f1:
        f1.write(s)


if __name__ == '__main__':
    paste('files/cat1.txt', 'files/cat2.txt')
