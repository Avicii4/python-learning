"""
用户输入一个目录和文件名，搜索该目录及其子目录，判断是否存在该文件
"""
import os


def search_file(path, file_name):
    if not isinstance(path, str) or not isinstance(file_name, str):
        print('文件名及路径类型错误')
        return
    tree = os.walk(path)
    for root, dirs, files in tree:
        if file_name in files:
            return True
    return False


if __name__ == '__main__':
    path = 'E:\\Books'
    fname = '1-4729.OBJ'
    print(search_file(path, fname))
