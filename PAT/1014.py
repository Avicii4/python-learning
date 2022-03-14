if __name__ == '__main__':
    strings = []
    for i in range(4):
        strings.append(input())
    weekdays = ('MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN')
    day = hour = minute = ''
    for a, b in zip(strings[0], strings[1]):
        if a == b and 'A' <= a <= 'G' and day == '':
            day = a
        elif a == b and day != '':
            if ord(a) in range(48, 58):
                hour = int(a)
                break
            elif ord(a) in range(65, 79):
                hour = ord(a) - 55
                break
    for i in range(min(len(strings[2]), len(strings[3]))):
        if strings[2][i] == strings[3][i] and \
                ('A' <= strings[2][i] <= 'Z' or 'a' <= strings[2][i] <= 'z'):
            minute = str(i)
            break

    print('{} {:0>2}:{:0>2}'.format(weekdays[ord(day) - 65], hour, minute))
