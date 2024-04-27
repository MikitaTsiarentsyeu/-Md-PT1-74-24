from backend import DataStorage

def main():
    data_storage = DataStorage("collection.json")
    data_storage.load_data()

    while True:
        print("\nMenu:")
        print("1. Add a new album or movie")
        print("2. List all albums or movies")
        print("3. Search for an album or movie")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title: ")
            artist_director = input("Enter the artist/director: ")
            year = input("Enter the year: ")
            genre = input("Enter the genre: ")
            item = {"title": title, "artist_director": artist_director, "year": year, "genre": genre}
            data_storage.add_item(item)
            print("Item added successfully!")

        elif choice == "2":
            items = data_storage.list_items()
            if not items:
                print("No items found.")
            else:
                print("\nList of all albums or movies:")
                for item in items:
                    print(item)

        elif choice == "3":
            search_term = input("Enter the keyword to search: ")
            search_category = input("Enter the category to search (title/artist_director/year/genre): ")
            search_results = data_storage.search_items(search_term, search_category)
            if not search_results:
                print("No matching items found.")
            else:
                print("\nSearch results:")
                for item in search_results:
                    print(item)

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
