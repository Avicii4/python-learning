"""
将保存学生成绩的字典存为二进制文件，再读取展示
"""
import pickle

if __name__ == '__main__':
    names = ['Jim', 'Tony', 'Tommy', 'Jessica', 'Anna']
    grades = [92, 66, 70, 88, 96]
    dic = dict(zip(names, grades))
    f = open('files/grade.dat', 'wb')
    try:
        pickle.dump(dic, f)
    except BaseException:
        print('写入异常')
    finally:
        f.close()
    f = open('files/grade.dat', 'rb')
    print(pickle.load(f))
