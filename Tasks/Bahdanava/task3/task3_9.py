#First option

x = "Hello, world"
x_reversed = x[::-1]
print(x_reversed)

#Second option

x = "Hello world!"
x_reversed = " "
for i in x:
    x_reversed = i + x_reversed
print(x_reversed)

#Third option

x = "Today is a wonderful day"
print(x[::-1])