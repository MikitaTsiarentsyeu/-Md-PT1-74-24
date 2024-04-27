user_input = list(input("input random numbers separated by space: ").split(" "))

s = 0

for i in user_input:
    if int(i) % 2 == 0 :
        s = s + int(i)
print("the sum of all aven numbers is ", s )