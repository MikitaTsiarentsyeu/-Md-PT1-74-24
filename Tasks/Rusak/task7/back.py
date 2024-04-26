import json
import os

class DataStorage:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                self.data = json.load(file)

    def save_data(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def add_item(self, item):
        self.data.append(item)
        self.save_data()

    def list_items(self):
        return self.data

    def search_items(self, keyword, category):
        results = []
        for item in self.data:
            if keyword.lower() in item[category].lower():
                results.append(item)
        return results
