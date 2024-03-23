# Implement a text output of the time entered from the console (the user should input data
# in the format hh:mm).
# Show the responses to the user in Russian according to the rules listed below:
#  min == 0: такое-то значение часа ровно (15:00 - три часа ровно)
#  min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)
#  min == 30: половина такого-то (15:30 - половина четвёртого)
#  min > 30 and min < 45 столько-то минут следующего часа (12:38 - тридцать восемь минут первого)
#  min >= 45 без min такого-то (08:54 - без шести минут девять)
user_data = input("Input time data in the format 'hh:mm': ")
if user_data[2] != ':':
    print(f"incorrect value, please check format 'hh:mm', your value is {user_data}")
    exit()
if int(user_data[0:2]) > 24:
    print(f"incorrect value, use 24 time format, your value is {user_data}")
    exit()
if int(user_data[3:]) > 60:
    print(f"incorrect value of minutes, your value is {user_data}")
    exit()
linguistic_dict = {
                    "00": {"00": "полночь",
                           "01": "первого"},
                    "01": {"00": "час",
                           "01": "второго",
                           "02": "одна",
                           "03": "одной"},
                    "02": {"00": "два",
                           "03": "двух",
                           "02": "две",
                           "01": "третьего"},
                    "03": {"00": "три",
                           "03": "трех",
                           "02": "три",
                           "01": "четвертого"},
                    "04": {"00": "четыре",
                           "03": "четырех",
                           "02": "четыре",
                           "01": "пятого"},
                    "05": {"00": "пять",
                           "03": "пяти",
                           "02": "пять",
                           "01": "шестого"},
                    "06": {"00": "шесть",
                           "03": "шести",
                           "02": "шесть",
                           "01": "седьмого"},
                    "07": {"00": "семь",
                           "03": "семи",
                           "02": "семь",
                           "01": "восьмого"},
                    "08": {"00": "восемь",
                           "03": "восьми",
                           "02": "восемь",
                           "01": "девятого"},
                    "09": {"00": "девять",
                           "03": "девяти",
                           "02": "девять",
                           "01": "десятого"},
                    "10": {"00": "десять",
                           "03": "десяти",
                           "02": "десять",
                           "01": "одиннадцатого"},
                    "11": {"00": "одиннадцать",
                           "03": "одиннадцати",
                           "02": "одиннадцать",
                           "01": "двенадцатого"},
                    "12": {"00": "двенадцать",
                           "03": "двенадцати",
                           "02": "двенадцать",
                           "01": "первого"},
                    "13": {"00": "час",
                           "03": "тринадцати",
                           "02": "тринадцать",
                           "01": "второго"},
                    "14": {"00": "два",
                           "03": "четырнадцати",
                           "02": "четырнадцать",
                           "01": "третьего"},
                    "15": {"00": "три",
                           "03": "пятнадцати",
                           "02": "пятнадцать",
                           "01": "четвертого"},
                    "16": {"00": "четыре",
                           "03": "шестнадцати",
                           "02": "шестнадцать",
                           "01": "пятого"},
                    "17": {"00": "пять",
                           "01": "шестого",
                           "02": "семнадцать"},
                    "18": {"00": "шесть",
                           "02": "восемнадцать",
                           "01": "седьмого"},
                    "19": {"00": "семь",
                           "02": "девятнадцать",
                           "01": "восьмого"},
                    "20": {"00": "восемь",
                           "02": "двадцать",
                           "01": "девятого"},
                    "21": {"00": "девять",
                           "01": "десятого",
                           "02": "двадцать одна"},
                    "22": {"00": "десять",
                           "02": "двадцать две",
                           "01": "одиннадцатого"},
                    "23": {"00": "одиннадцать",
                           "02": "двадцать три",
                           "01": "двенадцатого"},
                    "24": {"00": "полночь",
                           "02": "двадцать четыре",
                           "01": "первого"},
                    "25": {"02": "двадцать пять"},
                    "26": {"02": "двадцать шесть"},
                    "27": {"02": "двадцать семь"},
                    "28": {"02": "двадцать восемь"},
                    "29": {"02": "двадцать девять"},
                    "30": {"30": "половина",
                           "00": "тридцать"},
                    "40": {"00": "сорок"},
                    }

hour = user_data[0:2]
minutes = user_data[3:]

if minutes == "00":
    if hour == "24" or "00":
        data = linguistic_dict.get(hour).get("00")
        print(f"{hour}:00 - {data}")
    if hour in ["01", "13"]:
        data = linguistic_dict.get(hour).get("00")
        print(f"{hour}:00 - {data} час ровно")
    if hour in ["02", "03", "04", "14", "15", "16"]:
        data = linguistic_dict.get(hour).get("00")
        print(f"{hour}:00 - {data} часа ровно")
    if hour in ["05", "06", "07", "08", "09", "10", "11", "12", "17", "18", "19", "20", "21", "22", "23"]:
        data = linguistic_dict.get(hour).get("00")
        print(f"{hour}:00 - {data} часов ровно")

if minutes < "30":
    hour_data = linguistic_dict.get(hour).get("01")
    minutes_data = linguistic_dict.get(minutes).get("02")
    if minutes in ["01", "21"]:
        print(f"{hour}:{minutes} - {minutes_data} минута {hour_data}")
    if minutes in ["02", "03", "04", "22", "23", "24"]:
        print(f"{hour}:{minutes} - {minutes_data} минуты {hour_data}")
    if minutes in ["05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "25",
                   "26", "27", "28", "29"]:
        print(f"{hour}:{minutes} - {minutes_data} минут {hour_data}")

if minutes == "30":
    hour_data = linguistic_dict.get(hour).get("01")
    print(f"{hour}:{minutes} - половина {hour_data}")

if 30 < int(minutes) < 45:
    hour_data = linguistic_dict.get(hour).get("01")
    if minutes[0] == "3":
        if minutes[1] == "1":
            minutes_first_value = linguistic_dict.get("30").get("00")
            minutes_second_value = linguistic_dict.get(f"0{minutes[1]}").get("02")
            print(f"{hour}:{minutes} - {minutes_first_value} {minutes_second_value} минута {hour_data}")
        if minutes[1] == ["2", "3", "4"]:
            minutes_first_value = linguistic_dict.get("30").get("00")
            minutes_second_value = linguistic_dict.get(f"0{minutes[1]}").get("02")
            print(f"{hour}:{minutes} - {minutes_first_value} {minutes_second_value} минуты {hour_data}")
        if minutes[1] == ["5", "6", "7", "8", "9"]:
            minutes_first_value = linguistic_dict.get("30").get("00")
            minutes_second_value = linguistic_dict.get(f"0{minutes[1]}").get("02")
            print(f"{hour}:{minutes} - {minutes_first_value} {minutes_second_value} минут {hour_data}")
    if minutes[0] == "4":
        if minutes[1] == "0":
            minutes_first_value = linguistic_dict.get("40").get("00")
            minutes_second_value = linguistic_dict.get(f"0{minutes[1]}").get("02")
            print(f"{hour}:{minutes} - {minutes_first_value} минут {hour_data}")
        if minutes[1] == "1":
            minutes_first_value = linguistic_dict.get("40").get("00")
            minutes_second_value = linguistic_dict.get(f"0{minutes[1]}").get("02")
            print(f"{hour}:{minutes} - {minutes_first_value} {minutes_second_value} минута {hour_data}")
        if minutes[1] == ["2", "3", "4"]:
            minutes_first_value = linguistic_dict.get("40").get("00")
            minutes_second_value = linguistic_dict.get(f"0{minutes[1]}").get("02")
            print(f"{hour}:{minutes} - {minutes_first_value} {minutes_second_value} минуты {hour_data}")

if int(minutes) >= 45:
    data = 60 - int(minutes)
    hour_delta = int(hour) + 1
    _hour = f"0{hour_delta}"
    if int(hour) < 10:
        hour_data = linguistic_dict.get(str(_hour)).get("00")
    else:
        hour_data = linguistic_dict.get(str(hour_delta)).get("00")
    if data < 10:
        minutes_data = linguistic_dict.get(str(f"0{data}")).get("03")
    else:
        minutes_data = linguistic_dict.get(str(data)).get("03")
    if minutes in ["45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58"]:
        print(f"{hour}:{minutes} - без {minutes_data} минут {hour_data}")
    if int(minutes) == 59:
        print(f"{hour}:{minutes} - без {minutes_data} минуты {hour_data}")
