hours = {
    0:"ноль",
    1:"один",
    2:"два",
    3:"три",
    4:"четыре",
    5:"пять",
    6:"шесть",
    7:"семь",
    8:"восемь",
    9:"девять",
    10:"десять",
    11:"одинадцать",
    12:"двенадцать"
}

hours_ogo = {
    #0:"нолевого",
    1:"первого",
    2:"второго",
    3:"третьего",
    4:"четвертого",
    5:"пятого",
    6:"шестого",
    7:"семого",
    8:"восемого",
    9:"девятого",
    10:"десятого",
    11:"одинадцатого",
    12:"двенадцатого"
}

minutes = {
    1:"одна",
    2:"две",
    3:"три",
    4:"четыре",
    5:"пять",
    6:"шесть",
    7:"семь",
    8:"восемь",
    9:"девять",
    10:"десять",
    11:"одинадцать",
    12:"двенадцать",
    13:"тренадцать",
    14:"четырнадцать",
    15:"пятнадцать",
    16:"шестнадцать",
    17:"семнадцать",
    18:"восемнадцать",
    19:"девятнадцать",
    20:"двадцать",
    30:"тридцать",
    40:"сорок",
    50:"пятьдесят",
}

while True:
    time = input("Write time in hh:mm format to get it in russian\n")

    try:
        hour, minute = time.split(":")
    except:
        print("wrong format")
        continue
    try:  
        hour = int(hour)
        minute = int(minute)
    except:
        print("not a number")
        continue

    if hour < 0 or hour > 23:
        print(hour, "wrong hour value")
        continue

    if minute < 0 or minute > 59:
        print(hour, "wrong minute value")
        continue

    if(hour >= 12): 
        hour = hour - 12

    if minute == 0:
        print(hours[hour], "часов ровно")
        continue

    if minute == 30:
        if(hour < 12): hour = hour + 1
        print("половина", hours_ogo[hour])
        continue

    if minute < 30:
        if(hour < 12): hour = hour + 1
        if(minute > 20):
            print(f"двадцать{minutes[minute - 20]} минут {hours_ogo[hour]}")
            continue
        print(f"{minutes[minute]} минут {hours_ogo[hour]}")
        continue

    if minute > 30 and minute < 45:
        if(hour < 12): hour = hour + 1
        if(minute > 30 and minute < 40):
            print(f"тридцать{minutes[minute - 30]} минут {hours_ogo[hour]}")
            continue
        if(minute < 45 and minute > 40):
            print(f"сорок{minutes[minute - 40]} минут {hours_ogo[hour]}")
            continue
        if(minute == 40):
            print(f"{minutes[minute]} минут {hours_ogo[hour]}")
            continue

    if minute >= 45:
        if(hour < 12): hour = hour + 1
        if(minute >= 45 and minute < 50):
            print(f"сорок{minutes[minute - 40]} минут {hours_ogo[hour]}")
            continue
        if(minute == 50):
            print(f"{minutes[minute]} минут {hours_ogo[hour]}")
            continue
        if(minute > 50 and minute < 60):
            print(f"пятьдесят{minutes[minute - 50]} минут {hours_ogo[hour]}")
            continue


