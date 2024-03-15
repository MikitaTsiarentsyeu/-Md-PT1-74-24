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

if day > 31:
    print("incorrect value, the day value is too high")
    exit()

print(day, month, year)