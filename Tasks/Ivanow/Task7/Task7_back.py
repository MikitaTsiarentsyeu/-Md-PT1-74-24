
class Movie:
    movies_count = 0

    def __init__(self):
        Movie.movies_count += 1
        self.movies_count = Movie.movies_count
        self.title = input('Input title: ')
        self.director = input('Input director: ')
        self.year = input('Input year: ')
        self.genre = input('Input genre: ')

    def displayMovie(self):
        print(f'Title: {self.title}\tDirector: {self.director}\tYear:{self.year}\tGenre:{self.genre}')


movies = []


def add_new():
    movies.append(Movie())
    save_films()



def show_all():
    if len(movies) == 0:
        print('No movies now...')
    else:
        for i in range(len(movies)):
            movies[i].displayMovie()


def search(option, search_cond):
    if option == '1':
        if len(movies) == 0:
            print('No movies now...')
        else:
            for i in range(len(movies)):
                if movies[i].title == search_cond:
                    movies[i].displayMovie()
                else:
                    print('nothing found!')
    elif option == '2':
        if len(movies) == 0:
            print('No movies now...')
        else:
            for i in range(len(movies)):
                if movies[i].director == search_cond:
                    movies[i].displayMovie()
                else:
                    print('nothing found!')
    elif option == '3':
        if len(movies) == 0:
            print('No movies now...')
        else:
            for i in range(len(movies)):
                if movies[i].year == search_cond:
                    movies[i].displayMovie()
                else:
                    print('nothing found!')
    elif option == '4':
        if len(movies) == 0:
            print('No movies now...')
        else:
            for i in range(len(movies)):
                if movies[i].genre == search_cond:
                    movies[i].displayMovie()
                else:
                    print('nothing found!')


def save_films():
    with open('movies.txt','w') as f:
        for i in range(len(movies)):
            f.write(f'Title: {movies[i].title}\tDirector: {movies[i].director}\tYear: {movies[i].year}\tGenre: {movies[i].genre}\n')
    f.close()