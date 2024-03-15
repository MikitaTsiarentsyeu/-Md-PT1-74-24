time = input("Enter the time in the format hh:mm:\n")

if len(time) != 5:
    print("Invalid value, please enter the data in the specified format.")
    exit()

if time[2] != ":":
    print("Invalid value, please enter the data in the specified format.")
    exit()

hh, mm = time.split(':')

is_valid = True
if not hh.isdigit():
    print("The value is incorrect, please use only numbers to indicate the hours.")
    is_valid = False

if not mm.isdigit():
    print("The value is incorrect, please use only numbers to indicate the minutes.")
    is_valid = False
if not is_valid:
    exit()

hh = int(hh)

if hh > 23:
    print("The value is incorrect, please use only the numbers from 00 to 23 to indicate the hours.")
    is_valid = False

if int(mm) > 59:
    print("The value is incorrect, please use only the numbers from 00 to 59 to indicate the minutes.")
    is_valid = False

if not is_valid:
    exit()

if hh >= 12:
    hh %= 12

hh = str(hh)

if len(hh) == 1:
    hh = '0' + hh

hours_dict = {
    '00': ['двенадцать', 'первого', 'час'],
    '01': ['один', 'второго', 'два'],
    '02': ['два', 'третьего', 'три'],
    '03': ['три', 'четвертого', 'четыре'],
    '04': ['четыре', 'пятого', 'пять'],
    '05': ['пять', 'шестого', 'шесть'],
    '06': ['шесть', 'седьмого', 'семь'],
    '07': ['семь', 'восьмого', 'восемь'],
    '08': ['восемь', 'девятого', 'девять'],
    '09': ['девять', 'десятого', 'десять'],
    '10': ['десять', 'одинадцатого', 'одиннадцать'],
    '11': ['одиннадцать', 'двенадцатого', 'двенадцать']
}

minutes_dict = {
    '01': ['одна', 'одной'], '02': ['две', 'двух'], '03': ['три', 'трех'],
    '04': ['четыре', 'четырех'], '05': ['пять', 'пяти'],
    '06': ['шесть', 'шести'], '07': ['семь', 'семи'],
    '08': ['восемь', 'восьми'], '09': ['девять', 'девяти'],
    '10': ['десять', 'десяти'], '11': ['одиннадцать', 'одиннадцати'],
    '12': ['двенадцать', 'двенадцати'], '13': ['тринадцать', 'тринадцати'],
    '14': ['четырнадцать', 'четырнадцати'], '15': ['пятнадцать', 'пятнадцати'],
    '16': 'шестнадцать', '17': 'семнадцать', '18': 'восемнадцать',
    '19': 'девятнадцать', '20': 'двадцать', '30': ['половина', 'тридцать'],
    '40': 'сорок', '50': 'пятьдесят', '00': 'ровно'
}

# Declension of the word "hour".
if hh == '01':
    value_hour = 'час'
elif hh == '02' or hh == '03' or hh == '04':
    value_hour = 'часа'
else:
    value_hour = 'часов'

# Declension of the word "minute".
if (mm[0] == '1' or mm[0] == '5') and (mm[1] == '1' or mm[1] == '2' or mm[1] == '3' or mm[1] == '4'):
    value_min = 'минут'
elif mm[1] == '1':
    value_min = 'минута'
elif mm == '59' or mm[1] == '2' or mm[1] == '3' or mm[1] == '4':
    value_min = 'минуты'
else:
    value_min = 'минут'


if mm == '00':
    print(hours_dict[hh][0], value_hour, minutes_dict[mm])
elif int(mm) < 30:
    if mm[0] == '0':
        print(minutes_dict[mm][0], value_min, hours_dict[hh][1])
    elif mm[0] == '1':
        if int(mm[1]) < 6:
            print(minutes_dict[mm][0], value_min, hours_dict[hh][1])
        else:
            print(minutes_dict[mm], value_min, hours_dict[hh][1])
    else:
        if mm[1] == '0':
            print(minutes_dict['20'], value_min, hours_dict[hh][1])
        else:
            print(minutes_dict['20'], minutes_dict['0' + mm[1]][0],
                  value_min, hours_dict[hh][1])
elif mm == '30':
    print(minutes_dict[mm][0], hours_dict[hh][1])
elif '30' < mm < '45':
    if mm[0] == '3':
        print(minutes_dict['30'][1], minutes_dict['0' + mm[1]][0],
              value_min, hours_dict[hh][1])
    if mm[0] == '4':
        if mm[1] == '0':
            print(minutes_dict['40'], value_min, hours_dict[hh][1])
        else:
            print(minutes_dict['40'], minutes_dict['0' + mm[1]][0],
                  value_min, hours_dict[hh][1])
else:
    mm = str(60 - int(mm))
    if len(mm) == 1:
        mm = '0' + mm
    print(f'без {minutes_dict[mm][1]} {value_min} {hours_dict[hh][2]}')
