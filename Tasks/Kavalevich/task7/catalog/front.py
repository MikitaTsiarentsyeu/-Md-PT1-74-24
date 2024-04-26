import back

def show_all():
    print(back.show_all())

def add_movie():
    values = []
    for attr in back.attrs:
        value = input(f"Please enter movie {attr} value: ")
        values.append(value)
    
    try:
        back.add_movie(*values)
        print("\nThe movie was added")
    except RuntimeError as e:
        print(e)

def search_value():
    return input(f"Please enter {back.attrs[0]} value: ")
    
def search():
    value = search_value()
    print(back.search(value))

def delete_movie():
    value = search_value()
    print(back.delete_movie(value))

def start():
    while True:
        ch = input(f"""Choose a point of menu:
                   0. Exit
                   1. Show all movies
                   2. Add a movie
                   3. Search by {back.attrs[0]}
                   4. Remove a movie\n
                   """)
        if ch == '0':
            print("Have a good day!")
            break
        elif ch == '1':
            show_all()
        elif ch == '2':
            add_movie()
        elif ch == '3':
            search()
        elif ch == '4':
            delete_movie()
        else:
            print("Unknown option, please try again")
