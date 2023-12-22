class Movie:
    def __init__(self, title: str, place: str, time: str):
        self.title = title
        self.place = place
        self.time = time


test_movie = Movie("Железный человек 2", "Восток", "12:00")


def book_movie(movie: Movie) -> str:
    wish_template = '''Билет на " %s " в " %s " на %s забронирован.'''
    return wish_template % (movie.title, movie.place, movie.time)

# Всем привет

print(book_movie(test_movie))
