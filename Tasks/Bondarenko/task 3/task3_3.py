line = "hello hello hello world"
dictionary = {}

line = line.strip()
result = line.split()

for i in result:
    if i in dictionary:
        dictionary[i] = dictionary[i] + 1 
        continue
    dictionary[i] = 1

print(dictionary)

