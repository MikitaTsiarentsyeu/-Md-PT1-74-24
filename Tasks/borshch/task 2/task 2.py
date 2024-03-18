time = input('please, insert time value in format hh.mm:\n')

if len(time) != 5 or time[2] != ".":
    raise Exception("incorrect time format, please insert correct time value")

hours, minutes = time.split(".")

if not hours.isdigit() or not minutes.isdigit():
    raise Exception("incorrect time format, please use only digits for time value")

time = float(time)
if time > 24:
    raise Exception("incorrect time format, please insert correct time value")

hours, minutes = int(hours), int(minutes)
if hours > 24 or minutes > 59:
    raise Exception("incorrect time format, please insert correct time value")
if hours > 12:
    hours %= 12
hours, minutes = str(hours), str(minutes)

print(type(time), time, hours, type(hours), minutes, type(minutes))

numbers = {
    "0": '',
    "1": 'один',
    "2": 'два',
    "3": 'три',
    "4": 'четыре',
    "5": 'пять',
    "6": 'шесть',
    "7": 'семь',
    "8": 'восемь',
    "9": 'девять',
    "10": 'десять',
    "11": 'одиннадцать',
    "12": 'двеннадцать',
    "13": 'тринадцать',
    "14": 'четырнадцать',
    "15": 'пятнадцать',
    "16": 'шестнадцать',
    "17": 'семнадцать',
    "18": 'восемнадцать',
    "19": 'девятнадцать',
    "20": 'двадцать',
}
h = "час"
m = "минут"
if minutes == "0":
    if hours == "0":
        numbers ["0"] = "полночь"
        h = ""
    elif hours == "1":
        h = h
    elif "2" <= hours <= "4":
        h += "а"
    else:
        h += "ов"
    print(numbers[hours], h, "ровно")
if minutes != "0":
    hours = int(hours)
    hours += 1
    hours = str(hours)
    print(hours)

    if minutes == "30":
        if hours == "1" or hours == "13":
            numbers[hours] = numbers[hours].replace(numbers[hours], "первого")
        elif hours == "2":
            numbers[hours] = numbers[hours].replace(numbers[hours], "второго")
        elif hours == "3":
            numbers[hours] = numbers[hours].replace(numbers[hours], "третьего")
        elif hours == "4":
            numbers[hours] = numbers[hours].replace(numbers[hours], "четвертого")
        elif hours == "7":
            numbers[hours] = numbers[hours].replace(numbers[hours], "седьмого")
        elif hours == "8":
            numbers[hours] = numbers[hours].replace(numbers[hours], "восьмого")
        else:
            numbers[hours] = numbers[hours].replace(numbers[hours][-1], "ого")
        print("половина", numbers[hours])
    else:
        minutes = int(minutes)
        if 45 <= minutes <= 59:
            minutes1 = 60 - minutes
            minutes1 = str(minutes1)
            if hours == "1" or hours == "13":
                numbers[hours] = "час"
            if minutes1 == "1":
                t = "одной"
                m += "ы"
            elif minutes1 == "2":
                t = "двух"
            elif minutes1 == "3":
                t = "трех"
            elif minutes1 == "4":
                t = "четырех"
            else:
                t = numbers[minutes1].replace(numbers[minutes1][-1], "и")
            print("без", t, m, numbers[hours])
        elif 0 < minutes < 45:
            if str(minutes)[0] == "1" or (len(str(minutes)) == 2 and str(minutes)[0] != "1" and str(minutes)[1] == "1"):
                m += "а"
                numbers["1"] = "одна"
            if (len(str(minutes)) == 1 and str(minutes)[0] in ["2", "3", "4"]) or (len(str(minutes)) == 2 and str(minutes)[1] in ["2", "3", "4"]):
                m += "ы"
                if (len(str(minutes)) == 1 and str(minutes)[0] == "2") or (len(str(minutes)) == 2 and str(minutes)[1] == "2"):
                    numbers["2"] = "две"
            if len(str(minutes)) == 2 and str(minutes)[0] == "4":
                numbers["4"] = "сорок "
                numbers[str(minutes)] = numbers[str(minutes)[0]].__add__(numbers[str(minutes)[1]])
            elif len(str(minutes)) == 2 and str(minutes)[0] != "1":
                numbers[str(minutes)] = numbers[str(minutes)[0]].__add__("дцать ").__add__(numbers[str(minutes)[1]])


            if hours == "1" or hours == "13":
                numbers[hours] = numbers[hours].replace(numbers[hours], "первого")
            elif hours == "2":
                numbers[hours] = numbers[hours].replace(numbers[hours], "второго")
            elif hours == "3":
                numbers[hours] = numbers[hours].replace(numbers[hours], "третьего")
            elif hours == "4":
                numbers[hours] = numbers[hours].replace(numbers[hours], "четвертого")
            elif hours == "7":
                numbers[hours] = numbers[hours].replace(numbers[hours], "седьмого")
            elif hours == "8":
                numbers[hours] = numbers[hours].replace(numbers[hours], "восьмого")
            else:
                numbers[hours] = numbers[hours].replace(numbers[hours][-1], "ого")

            if minutes == 22:
                numbers[str(minutes)] = "двадцать две"
                print(numbers[str(minutes)], m, numbers[hours])
                exit()
            if minutes == 44:
                numbers[str(minutes)] = "сорок четыре"
                print(numbers[str(minutes)], m, numbers[hours])
                exit()

            print(numbers[str(minutes)], m, numbers[hours])
