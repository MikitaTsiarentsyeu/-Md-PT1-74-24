from backend import Collection

def menu():
    print("\nMenu:")
    print("1. Add a new item to the collection")
    print("2. List all items in the collection")
    print("3. Search for an item")
    print("4. Quit")

def add_item(collection):
    title = input("Enter title: ").strip()
    artist = input("Enter artist/director: ").strip()  
    year = input("Enter year: ").strip()
    genre = input("Enter genre: ").strip()

    if title and artist and year and genre:  
        collection.add_item({
            "title": title,
            "artist": artist,  
            "year": year,
            "genre": genre
        })
        print("Item added successfully!")
    else:
        print("Please fill in all fields.")

def list_items(collection):
    if collection:
        print("\nAll items in the collection:")
        for item in collection:
            print(f"Title: {item['title']}, Artist/Director: {item['artist']}, Year: {item['year']}, Genre: {item['genre']}")
    else:
        print("The collection is empty.")

def search_item(collection):
    search_criteria = input("Enter search criteria (title/artist/year/genre): ").strip().lower()
    search_value = input(f"Enter {search_criteria} to search for: ").strip().lower()

    results = collection.search(search_criteria, search_value)
    if results:
        print("\nSearch Results:")
        for item in results:
            print(f"Title: {item['title']}, Artist/Director: {item['artist']}, Year: {item['year']}, Genre: {item['genre']}")
    else:
        print("No matching items found.")

if __name__ == "__main__":
    collection = Collection("music.json")
    while True:
        menu()
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_item(collection)
        elif choice == '2':
            list_items(collection.collection)
        elif choice == '3':
            search_item(collection)
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice!")
