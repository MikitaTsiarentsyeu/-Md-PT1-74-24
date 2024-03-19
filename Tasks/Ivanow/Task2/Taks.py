time = input('Input time in next format hh:mm (if 5AM -> 05:00):\t')

valid_input = True

if len(time) > 5:
    valid_input = False
elif time[2] != ':':
    valid_input = False

if not valid_input:
    print('Incorrect input! Check formation!')
    exit()

hours, minutes = time.split(':')

if not hours.isdigit():
    valid_input = False
elif not minutes.isdigit():
    valid_input = False

if not valid_input:
    print('Incorrect input! Use digits in hours/minutes input!')
    exit()

hours, minutes = int(hours), int(minutes)
minutes_first = (minutes // 10) * 10
minutes_second = minutes - minutes_first

if hours < 0 or hours > 25:
    valid_input = False
elif minutes < 0 or minutes > 59:
    valid_input = False

if not valid_input:
    print('Incorrect input! Hours/minutes over limit (24/59)!')
    exit()

after_midday = False

if hours > 12:
    hours = hours - 12
    after_midday = True
elif hours == 0:
    hours = 12

hours_text = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять',
              10: 'десять', 11: 'одиннадцать', 12: 'двенадцать'}
hours_additional_text = {1: 'первого', 2: 'второго', 3: 'третьего', 4: 'четвёртого', 5: 'пятого', 6: 'шестого',
                         7: 'седьмого', 8: 'восьмого', 9: 'девятого', 10: 'десятого', 11: 'одиннадцатого',
                         12: 'двенадцатого'}
minutes_text = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять',
                10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать',
                15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнцадцать',
                20: 'двадцать', 30: 'тридцать', 40: 'сорок'}
minutes_additional_text = {1: 'одной', 2: 'двух', 3: 'трёх', 4: 'четырёх', 5: 'пяти', 6: 'шести', 7: 'семи',
                           8: 'восьми', 9: 'девяти', 10: 'десяти', 11: 'одиннадцати', 12: 'двенадцати',
                           13: 'тринадцати', 14: 'четырнадцати', 15: 'пятнадцати'}

if minutes == 0:
    if hours > 4:
        if after_midday:
            print(f'{hours_text[hours]} часов после полудня ровно')
        else:
            print(f'{hours_text[hours]} часов ровно')
    else:
        if after_midday:
            print(f'{hours_text[hours]} часа после полудня ровно')
        else:
            print(f'{hours_text[hours]} часа ровно')
elif minutes < 30:
    hours = hours + 1
    if hours > 12:
        hours = hours - 12
    if minutes < 20:
        if after_midday:
            print(f'{minutes_text[minutes]} минут {hours_additional_text[hours]} после полудня')
        else:
            print(f'{minutes_text[minutes]} минут {hours_additional_text[hours]}')
    else:
        if after_midday:
            if minutes == 21:
                print(f'{minutes_text[minutes_first]} {minutes_text[minutes_second][:2]}на минут {hours_additional_text[hours]} после полудня')
            elif minutes == 22:
                print(f'{minutes_text[minutes_first]} {minutes_text[minutes_second][:2]}е минут {hours_additional_text[hours]} после полудня')
            else:
                print(f'{minutes_text[minutes_first]} {minutes_text[minutes_second]} минут {hours_additional_text[hours]} после полудня')
        else:
            if minutes == 21:
                print(f'{minutes_text[minutes_first]} {minutes_text[minutes_second][:2]}на минут {hours_additional_text[hours]} после полудня')
            elif minutes == 22:
                print(f'{minutes_text[minutes_first]} {minutes_text[minutes_second][:2]}е минут {hours_additional_text[hours]} после полудня')
            else:
                print(f'{minutes_text[minutes_first]} {minutes_text[minutes_second]} минут {hours_additional_text[hours]}')
elif minutes == 30:
    hours = hours + 1
    if hours > 12:
        hours = hours - 12
    if after_midday:
        print(f'половина {hours_additional_text[hours]} после полудня')
    else:
        print(f'половина {hours_additional_text[hours]}')
elif minutes < 45:
    hours = hours + 1
    if hours > 12:
        hours = hours - 12
    if after_midday:
        print(
            f'{minutes_text[minutes_first]} {minutes_text[minutes_second]} минут {hours_additional_text[hours]} после полудня')
    else:
        print(f'{minutes_text[minutes_first]} {minutes_text[minutes_second]} минут {hours_additional_text[hours]}')
elif minutes >= 45:
    hours = hours + 1
    if hours > 12:
        hours = hours - 12
    minutes = 60 - minutes
    if after_midday:
        print(f'без {minutes_additional_text[minutes]} минут {hours_text[hours]} после полудня')
    else:
        print(f'без {minutes_additional_text[minutes]} минут {hours_text[hours]}')
