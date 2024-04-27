import Task7_back


def add_new():
    Task7_back.add_new()
    pass


def show_all():
    try:
        Task7_back.show_all()
    except:
        print('error')


def search():
    while True:
        ch = input('''Choose:
                            0. Exit
                            1. Search by title
                            2. Search by director
                            3. Search by year
                            4. Search by genre
                ''')
        if ch == '0':
            print('Complete')
            break
        elif ch == '1':
            src_cond = input('Input title: ')
            Task7_back.search(ch,src_cond)
        elif ch == '2':
            src_cond = input("Input director's name: ")
            Task7_back.search(ch, src_cond)
        elif ch == '3':
            src_cond = input('Input year: ')
            Task7_back.search(ch, src_cond)
        elif ch == '4':
            src_cond = input('Input genre: ')
            Task7_back.search(ch, src_cond)
        else:
            print('Wrong input!')


def start():
    while True:
        ch = input('''Choose:
                    0. Exit
                    1. Show all movies in library
                    2. Add new movie to library
                    3. Search movie
        ''')
        if ch == '0':
            print('bye!')
            break
        elif ch == '1':
            show_all()
        elif ch == '2':
            add_new()
        elif ch == '3':
            search()
        else:
            print('Wrong input!')
