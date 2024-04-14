import back

def show_all():
    try:
        res = back.show_all()
        print(res)
    except RuntimeError as e:
        print(e)
    except:
        print("something went wrong, please try again later")

def add_product():
    values = []
    for attr in back.attrs:
        value = input(f"please enter product {attr} value:")
        values.append(value)
    try:
        back.add_product(*values)
        print("the product was added")
    except RuntimeError as e:
        print(e)

def remove_product():
    value = enter_search_q()
    print(back.remove_product(value))

def search():
    value = enter_search_q()
    print(back.search(value))

def enter_search_q():
    return input(f"please enter the {back.attrs[0]} to search:")

def start():

    while True:
        ch = input(f"""Choose a point of menu:
                   0. exit
                   1. show all products
                   2. add a product
                   3. remove a product
                   4. search by {back.attrs[0]}\n
            """)
        if ch == '0':
            print("have a nice day")
            break
        elif ch == '1':
            show_all()
        elif ch == '2':
            add_product()
        elif ch == '3':
            remove_product()
        elif ch == '4':
            search()
        else:
            print("unknown option, please try again")