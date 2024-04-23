# info = [{"title": "The next episode", "artist(director)": "Dr. Dre ft. Snoop Dogg", "genre": "rap", "year": "2000"},
#         {"title": "Beautiful", "artist(director)": "Snoop Dogg ft. Pharell Williams", "genre": "rap", "year": "2002"},
#         {"title": "Fast and Furious", "artist(director)": "Neal Moritz", "genre": "action", "year": "2001"},
#         {"title": "P.I.M.P", "artist(director)": "50 Cent", "genre": "rap", "year": "2003"}]
import json

params = ["title", "artist(director)", "genre", "year"]


def add_info(*values):
    with open('info.json', 'r') as info:
        f = json.load(info)
        #info.writelines(",\n" + str(file))
        file = {}
        for i, param in enumerate(params):
            file[param] = values[i]
        f.append(file)

    with open('info.json', 'w') as info:
        json.dump(f, info)


def browse_all():
    with open('info.json', 'r') as info:
        info = json.load(info)
        if not info:
            raise Exception("There is no such file")
        return "\n".join([formated_info(p) for p in info])


def search_by_param(value):
    with open('info.json', 'r') as info:
        info = json.load(info)
        def search_gen():
            for i in info:
                if value in i.values():
                    yield formated_info(i)
        x = search_gen()
        if x:
            return "\n".join(j for j in x)
        return "noting was found"



def formated_info(file):
    return "; ".join([f"{k}: {v}" for k, v in file.items()])