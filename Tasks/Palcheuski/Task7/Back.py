import json
import os

inf_car = ['Car brand', 'Model', 'Year of release', 'Color']

def format_car(car):
     return '; '.join([f'{k}: {v}' for k, v in car.items()])

def add_car(*values):
    if not os.path.exists('cars.json'):
        with open('cars.json', 'w') as add_car:
            data = {
                'cars':[]
            }
            data['cars'] += values
            json.dump(data, add_car)
    else:
        with open('cars.json','r') as read_f:
            data = json.load(read_f)
            data['cars'] += values
            with open('cars.json', 'w') as add_car:
                json.dump(data, add_car)



def  show_all():
    with open('cars.json','r') as file_car:
        cars_info = json.load(file_car)
        return '\n'.join([format_car(p) for p in cars_info['cars']])
    

def search(fi, find_car):
    if os.path.exists('cars.json'):
        with open('cars.json','r') as r_find:
            data_find = json.load(r_find)

        b = []
        for f in data_find['cars']:
            if f[inf_car[fi]] == find_car:
                b.append('\n' + format_car(f))
        if b:
            return b
        else:
            return "Nothing was found"
    else:
        return 'No file to search'
    