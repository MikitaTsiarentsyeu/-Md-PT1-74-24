import json

#[{"title":"Master of Puppets", "artist":"Metallica", "year":"1986", "genre":"thrash-metal"},
#{"title":"Metallica", "artist":"Metallica", "year":"1991", "genre":"heavy-metal"}]

#data = ""

atr = ["title","artist","year","genre"]

def show_all():
    data = None
    dict = {}
    dict_list = []
    with open('data.json', 'r') as f:
        data = json.load(f)

    for item in data:
        for key, value in item.items():
            dict[key] = value

        dict_list.append(dict)
        dict = {}
    return dict_list

def add(*values):
    temp_dict = {}
    index = 0
    for i in atr:
        temp_dict[i] = values[index]
        index += 1

    new_dict_list = show_all()
    new_dict_list.append(temp_dict)

    with open('data.json', 'w') as f:
        json.dump(new_dict_list,f,indent = 4)    

def search(key, value):
    dict_list = show_all()
    new_dict_list = []
    for item in dict_list :
        for key_i, value_i in item.items():
            if str(key) == str(key_i) and str(value) == str(value_i):
                new_dict_list.append(item)
    return new_dict_list
    
