def kilometres_to_metres(kilometres_per_hour):
    metres_per_second = (kilometres_per_hour * 1000) / 3600
    return metres_per_second

kilometres_per_hour = int(input("Enter the speed in km/h: "))
metres_per_second = kilometres_to_metres(kilometres_per_hour)
print(metres_per_second)







def kilometres_to_metres(kilometres_per_hour):
    metres_per_second = (kilometres_per_hour * 1000) / 3600
    return metres_per_second

while True:
    kilometres_per_hour = input("Enter the speed in km/h (or type 'end' to exit): ")
    if kilometres_per_hour.lower() == 'end':
        break
    kilometres_per_hour = int(kilometres_per_hour)
    metres_per_second = kilometres_to_metres(kilometres_per_hour)
    rounded_speed = round(metres_per_second, 2)
    print("The speed in m/s is:", rounded_speed)





