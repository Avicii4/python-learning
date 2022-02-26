def third_person_singular(verb: str) -> str:
    lst = ['o', 'ch', 's', 'sh', 'x', 'z']
    if verb.endswith('y'):
        return verb[:-1] + 'ies'
    elif verb[-2:] in lst or verb[-1] in lst:
        return verb + 'es'
    else:
        return verb + 's'


if __name__ == '__main__':
    while True:
        word = input('请输入一个动词：')
        if word == '':
            exit('用户主动中止')
        print(third_person_singular(word))
