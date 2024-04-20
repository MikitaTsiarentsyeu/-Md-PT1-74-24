import Back

def add_car():
    
    values = {}
    for attr in Back.inf_car:
        vls = input(f'Please enter car information\n {attr} : ')
        values[attr] = vls
    try:
        Back.add_car(values)
        print('The car was added')
    except:
        print('Something went wrong,please try again later')


def  show_all():
    try:
        Sh_all = Back.show_all()
        print('''                  Cars:\n''')
        print(Sh_all)
    except FileNotFoundError:
        print('The file is missing or there is no entry at this time')
    except:
        print('Something went wrong,please try again later')


def search():
    while True:

        fi = input('''         ________________________
        | Search menu selection: |
        | 1 - Car brand          |
        | 2 - Model              |
        | 3 - Year of release    |
        | 4 - Color              |
        | 0 - Exit               |
        |________________________|\n''')
        
        if fi == '0':
            print('Happy searching next time')
            break
        elif fi in '1234':
            fi = int(fi) - 1
            find_car = input(f'Enter {Back.inf_car[fi]}: ')
            try:
                res = Back.search(fi,find_car)
                if type(res) == list:
                    print(*res)
                else:
                    print(res)
                break
            except:
                print('Something went wrong,please try again later')
        else:
            print('Please select the indicated menu item')




print('\n                  Welcom!')

while True:
    x = input('''         ________________________
        | Choose a point of menu:|
        | 1 - Show all cars      |
        | 2 - Add a car          |
        | 3 - Search a car       |
        | 0 - Exit programm      |
        |________________________|\n''')
    
    if x == '0':
        print('Have a good day')
        break
    elif x == '1':
        show_all()
    elif x == '2':
        add_car()
    elif x == '3':
        search()
    else:
        print('Please select the indicated menu item')
 



    
