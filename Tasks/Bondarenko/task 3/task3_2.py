list = [1, 2, 3, 0, 44, 20, -10, 5, 7]

#solution 1
print(f"sum of all even numbers = {sum([i for i in list if i % 2 == 0])}")

#solution 2
total = 0
for i in list:
    if i % 2 == 0:
        total = total + i

print(f"sum of all even numbers = {total}")

