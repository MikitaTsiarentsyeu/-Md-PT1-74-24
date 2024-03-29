import csv
import json
import pickle

with open('sniekers.csv', 'r') as csv_doc:
    reader = csv.reader(csv_doc)
    for line in reader:
        print(line)


with open('sniekers.csv', 'r') as csv_doc:
    reader = csv.DictReader(csv_doc)
    for line in reader:
        print(line)

with open("data.txt", 'r') as f:
    cars_data = eval(f.read())


with open('cars_data.csv', 'w', newline='') as csv_doc:
    writer = csv.writer(csv_doc)
    writer.writerows(cars_data)

# JSON

{
    "model": "superstar",
    "size": 40,
    "colors": ['red', 'blue'],
    "maker": {
        "name": "Adidas AG",
        "code": 65476
    }
}

# print(json.dumps(cars_data))

with open('cars_data.json', 'w') as f:
    json.dump(cars_data, f)

with open('cars_data.json', 'r') as f:
    cars_data_new = json.load(f)

print(cars_data == cars_data_new)
print(cars_data)
print(cars_data_new)


with open('cars_data.pickle', 'wb') as f:
    pickle.dump(cars_data, f)

with open('cars_data.pickle', 'rb') as f:
    cars_data_new = pickle.load(f)

print(cars_data == cars_data_new)

with open('print.pickle', 'wb') as f:
    pickle.dump(print, f)

with open('print.pickle', 'rb') as f:
    new_print = pickle.load(f)

new_print("test print from new_print")

# data = []

# with open('sniekers.csv', 'r') as csv_doc:
#     for line in csv_doc:
#         item = line.strip().split(',')
#         unite = False
#         united_value = ""
#         start = 0
#         end = 0
#         if '"' in line:
#             for i, param in enumerate(item):
#                 if param[0] == '"':
#                     unite = True
#                     start = i
#                 if param[-1] == '"':
#                     united_value = f"{united_value},{param}"[1:]
#                     unite = False
#                     end = i+1
#                 if unite:
#                     united_value = f"{united_value},{param}"
#         if united_value:
#             del item[start:end]
#             item.insert(start, united_value)
#         united_value = ""
#         data.append(item)

# # print(data)

# header = data[0]

# for item in data[1:]:
#     for i, value in enumerate(item):
#         print(f"{header[i]}:{value} ", end="")
#     print()

