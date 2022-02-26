def insert_name():
    with open('files/names.txt', 'r', encoding='utf-8') as f1:
        names = f1.readlines()
    add_name = input('Please input a new name:')
    if add_name == '':
        exit(-1)
    if add_name not in names:
        names.append(add_name + '\n')
    with open('files/new_names.txt', 'w', encoding='utf-8') as f2:
        f2.writelines(sorted(names))


if __name__ == '__main__':
    insert_name()
