def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print("Temperature in Fahrenheit: ", fahrenheit)









def fahrenheit_conversion(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

while True:
    celsius = input("Enter the temperature in Celsius (or type 'end' to exit): ")
    if celsius.lower() == 'end':
        break
    celsius = float(celsius)
    fahrenheit = fahrenheit_conversion(celsius)
    print("Temperature in Fahrenheit:", fahrenheit)
