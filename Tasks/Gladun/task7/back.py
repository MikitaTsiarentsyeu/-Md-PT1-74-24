import json

params = ["title", "artist(director)", "genre", "year"]


def show():
    with open('libery.json' , 'r') as info:
        file = {}
