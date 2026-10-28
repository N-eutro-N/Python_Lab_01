MY_FAVORITE_MOVIES = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'


def pick_movies(movies):

    return (
        movies[0:10],
        movies[42:],
        movies[12:25],
        movies[35:40],
    )


if __name__ == '__main__':
    for movie in pick_movies(MY_FAVORITE_MOVIES):
        print(movie)
