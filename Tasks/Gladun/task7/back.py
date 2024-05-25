import json

params = ["title", "artist(director)", "genre", "year"]


def show(*values):
    with open('libery.json' , 'r') as info:
        info = json.load(info)
        if not info:
            raise Exception("There is no such file")
        return "\n".join([formated_info(p) for p in info])

def formated_info(file):
    return "; ".join([f"{i}: {l}" for i, l in file.items()])

def add(*values):
    value = []
    with open('libery.json', 'r') as info:
        f = json.load(info)
        file = {}
        for i , param in enumerate(params):
            file[param] = values[i]
        f.append(file)

    with open('libery.json', 'w') as info:
        json.dump(f, info)