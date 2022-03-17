# 获取全部ETC记录，组成列表
import datetime


def get_record(file_name):
    with open('file/' + file_name, 'rt', encoding='utf-8') as f:
        vlst = f.readlines()
    return vlst


# 获取车辆信息集合
def get_v(vlst):
    vset = set()
    for v in vlst:
        vset.add(v[:10])
    return vset


# 记录车辆进出次数字典
def count_v(vlst, vset):
    freq = dict()
    name_lst = [v[:10] for v in vlst]
    for car in vset:
        freq[car] = name_lst.count(car)
    return freq


# 车辆累计停留时间字典
def count_t(vlst, vset):
    time_dict = dict()

    def time_cnt(etc_info):
        arr = etc_info.split('|')
        date = list(map(int, arr[1][:10].split('-')))
        t1 = map(int, arr[1][11:].split(':'))
        t2 = map(int, arr[2][11:].split(':'))
        start_time = datetime.datetime(*date, *t1)
        end_time = datetime.datetime(*date, *t2)
        return (end_time - start_time).seconds

    for info in vlst:
        info = info.strip()
        name = info[:10]
        time_dict[name] = time_dict.get(name, 0) + time_cnt(info)
    return time_dict


# 写入结果文件
def write_to_file(vlst, freq, inter, file_name):
    with open('file/' + file_name, 'w', encoding='utf-8') as f:
        f.write('记录条数：{}\n'.format(len(vlst)))
        f.write('车辆数：{}\n'.format(len(freq)))
        f.write('进校次数最多的5辆车（单位：次）：\n'.format())
        for n in sorted(freq, key=lambda x: -freq[x])[:5]:
            f.write('{}，{}\n'.format(n, freq[n]))
        f.write('累计停留时间最长的5辆车（单位：秒）：\n'.format())
        for n in sorted(inter, key=lambda x: -inter[x])[:5]:
            f.write('{}，{}\n'.format(n, inter[n]))


def main():
    vehicle_lst = get_record("data.txt")  # 读文件，获取全部ETC 记录，构成列表
    vehicle_set = get_v(vehicle_lst)  # 获取全部不同的ETC 编号，构成集合
    fre_dict = count_v(vehicle_lst, vehicle_set)  # 构造车辆进出校园次数的字典
    inter_dict = count_t(vehicle_lst, vehicle_set)  # 构造车辆累计停留时间的字典
    write_to_file(vehicle_lst, fre_dict, inter_dict, "report.txt")  # 输出结果到文件中
    return


main()  # 调用main 函数
