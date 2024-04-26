import json
import os

FILE = "movies.json"

attrs = ["Title", "Director", "Year of release", "Genre"]

with open(FILE, 'w') as f:
    json.dump([], f)

def read_file():
    with open(FILE, 'r') as f:
        return json.load(f)

def show_all():
    try:
        data = read_file()
        val = '\n'.join(format_movie(movie) for movie in data)
        if val:
            return val
        else:
            return "There are not movies right now."
    except (json.decoder.JSONDecodeError):
        return "There are not movies right now."

def add_movie(*values):
    if len(values)!= len(attrs):
        raise RuntimeError("Insufficient number attributes for add movie, "
                           "please try again.")
    
    with open(FILE, 'r') as f:
        content = f.read().strip()
    if not content:
        data = []
    else:
        data = read_file()
    movie = {}
    for i, attr in enumerate(attrs):
        movie[attr] = values[i]
    data.append(movie)
    with open(FILE, 'w') as f:
        json.dump(data, f)

def serch_value(value):
    data = read_file()
    for i, movie in enumerate(data):
        if movie[attrs[0]] == value:
            return data, i, movie
        
def search(value):
    try:
        movie = serch_value(value)
        if movie:
            return format_movie(movie[0][movie[1]])
        return "The value was not found."  
    except (json.decoder.JSONDecodeError):
        return "There are not movies right now."
    
def delete_movie(value):
    try:
        movie = serch_value(value)
        if movie:
            data = movie[0]
            del data[movie[1]]
            os.remove(FILE)
            with open(FILE, 'w') as f:
                json.dump(data, f)
            return "Movie was deleted."
        else:
            return "The value was not found."  
    except (json.decoder.JSONDecodeError):
        return "There are not movies right now."
    except:
        return "Something went wrong."    

def format_movie(movie):
    return ', '.join([f'{k}:{v}' for k, v in movie.items()]).replace(':', ': ')
    