def time_output():
    time_input = input("Введите время в формате hh:mm: ")
    hours, minutes = map(int, time_input.split(':'))

    if minutes == 0:
        print(f"{hours}:{minutes:02} - {hours} часов ровно")
    elif minutes < 30:
        print(f"{hours}:{minutes:02} - {minutes} минут следующего часа")
    elif minutes == 30:
        print(f"{hours}:{minutes:02} - половина {hours + 1}")
    elif minutes > 30 and minutes < 45:
        print(f"{hours}:{minutes:02} - {minutes} минут следующего часа")
    elif minutes >= 45:
        print(f"{hours}:{minutes:02} - без {60 - minutes} минут {hours + 1}")


if __name__ == "__main__":
    time_output()
