# day = input("enter you dob:\n")
# month = input("enter you mob:\n")
# year = input("enter you yob:\n")

date = input("enter you dob in the format dd.mm.yyyy:\n")

if len(date) != 10:
    print("incorrect value, please stick to the format next time")
    exit()

if date[2] != '.' or date[5] != '.':
    print("incorrect value, please stick to the format next time")
    exit()

day, month, year = date.split('.')

is_valid = True
if not day.isdigit():
    print("incorrect value, please use only digits for the day part")
    is_valid = False

if not month.isdigit():
    print("incorrect value, please use only digits for the month part")
    is_valid = False

if not year.isdigit():
    print("incorrect value, please use only digits for the year part")
    is_valid = False

if not is_valid:
    exit()

day, month, year = int(day), int(month), int(year)

# if day > 31:
#     print("incorrect value, the day value is too high")
#     exit()

# if month == 1:
#     if day > 31:
#         print("incorrect value, the day value is too high")
#         exit()
# elif month == 2:
#     if day > 29:
#         print("incorrect value, the day value is too high")
#         exit()
# elif month == 3:
#     if day > 31:
#         print("incorrect value, the day value is too high")
#         exit()
# elif month == 4:
#     if day > 30:
#         print("incorrect value, the day value is too high")
#         exit()


month_days = {
    1: 31,  # January
    2: 28,  # February
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

if year % 4 == 0:
    month_days[2] = 29

if month not in month_days:
    print("incorrect month value")
    exit()

if day > month_days[month]:
    print("incorrect value, the day value is too high")
    exit()

print(day, month, year)