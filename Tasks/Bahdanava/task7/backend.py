import json
import os

class Collection:
    def __init__(self, filename):
        self.filename = filename
        self.collection = self.load_collection()

    def load_collection(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            with open(self.filename, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Error: JSON file is not properly formatted.")
        return []

    def save_collection(self):
        with open(self.filename, 'w') as file:
            json.dump(self.collection, file, indent=4)

    def add_item(self, item):
        self.collection.append(item)
        self.save_collection()

    def list_items(self):
        for item in self.collection:
            print(item)

    def search(self, key, value):
        results = [item for item in self.collection if str(item.get(key, '')).lower() == value.lower()]
        return results
