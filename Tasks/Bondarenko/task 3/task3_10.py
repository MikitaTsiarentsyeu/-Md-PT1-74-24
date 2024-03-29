numbers = [1,2,3,4,5,6,7,8,9,10,0,11,12,50,100,97,11,23,56]

prime_numbers = []

counter = 0

for i in numbers:
    for j in numbers:
        if i > 1 and j != 0:
            if i % j == 0:
                counter += 1
    if counter == 2:
        prime_numbers.append(i)
    counter = 0

print(f"prime number list {prime_numbers}")
print(f"max prime number in list {max(prime_numbers)}")