import back_end

def add_info():
    values = []
    for param in back_end.params:
        value = input(f"please insert {param} value:\n")
        values.append(value)
    back_end.add_info(*values)
    print("file information was successfully added")

def browse_all():
    try:
        print(back_end.browse_all())
    except Exception as e:
        print(e)


def search_by_param():
    value = input("Please insert parameter to search:\n")
    print(back_end.search_by_param(value))


def user_interface():
    while True:
        ch = input(f""""Please choose wright point from menu below:
                    1. Add a new album or movie.
                    2. List all albums or movies.
                    3. Search for an album or movie by title, artist/director, year, or genre.
                    0. Quit the program.
                    """)
        if ch == "1":
            add_info()
        elif ch == "2":
            browse_all()
        elif ch == "3":
            search_by_param()
        elif ch == "0":
            print("Thank you for using our program.\nHave a nice day.")
            break
        else:
            print("Unknown operation, please try again")

