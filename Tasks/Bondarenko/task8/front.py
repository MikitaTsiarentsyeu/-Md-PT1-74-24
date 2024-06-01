import back

def show_all():
    try:
        result = back.show_all()
        for item in result:
            for key, value in item.items():
                print(f"{key} : {value}")
    except RuntimeError:
        print("RuntimeError")

def add():
    try:
        values = []
        for atr in back.atr:
            value = input(f"enter {atr} value: ")
            values.append(value)
        back.add(*values)
    
    except RuntimeError:
        print("RuntimeError")

def search():
    try:
        print("enter key value")
        print(f"avalible keys {back.atr}")
        key = input()
        if key in back.atr:
            print("enter value")
            value = input()
            result = back.search(key, value)

            if result == []:
                print(f"nothing was found with key '{key}' and value '{value}'")
            else:
                for item in result:
                    for key, value in item.items():
                        print(f"{key} : {value}")
        else:
            print(f"key '{key}' dont exist")
    except RuntimeError:
        print("RuntimeError")


while True:
    index = int(input(""
    "0. show all albums\n"
    "1. add new album\n"
    "2. search\n"
    "3. exit\n"
    ""))

    if index == 0:
        show_all()
    
    elif index == 1:
        add()
    
    elif index == 2:
        search()

    elif index == 3:
        break
    else:
        print("command dont exist")
    

