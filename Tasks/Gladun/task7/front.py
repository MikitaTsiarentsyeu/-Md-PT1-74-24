import back

def show():
    try:
        print(back.show())
    except:
        print("show error")

def add():
    values = []
    for param in back.params:
        value = input(f"please, insert {param}:\n")
        values.append(value)
    back.add(*values)
    print("file added")
def start():
    while True:
        user_input = input(""" Commands:
                        0. Exit
                        1. Show all
                        2. add file
        """)

        if user_input == '0':
            print("Have nice day")
            break
        elif user_input == '1':
            show()
        elif user_input == '2':
            add()
        else:
            print("Unknown operation, please try again")