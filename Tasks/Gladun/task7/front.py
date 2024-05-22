import back

def start():
    while True:
        user_input = input(""" Commands:
                        0. Exit
                        1. Show all
                        2. Add file
                        3. Search title
        """)

        if user_input == 0:
            print("Have nice day")
            break
        elif user_input == 1:
            show()
        elif user_input == 2:
            add_file()
        elif user_input == 3:
            searth()
        else:
            print("Unknown operation, please try again")