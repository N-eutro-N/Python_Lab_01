VIOLATOR_SONGS_LIST = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

VIOLATOR_SONGS_DICT = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}


def total_duration_list(songs, titles):
    return round(sum(duration for name, duration in songs if name in titles), 3)


def total_duration_dict(songs, titles):
    return round(sum(songs[title] for title in titles), 3)


if __name__ == '__main__':
    total_list = total_duration_list(
        VIOLATOR_SONGS_LIST, ('Halo', 'Enjoy the Silence', 'Clean'))
    print(f'Три песни звучат {total_list} минут')

    total_dict = total_duration_dict(
        VIOLATOR_SONGS_DICT, ('Sweetest Perfection', 'Policy of Truth', 'Blue Dress'))
    print(f'А другие три песни звучат {total_dict} минут')
