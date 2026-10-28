from solutions.task_00_distance import SITES, build_distances
from solutions.task_01_circle import RADIUS, circle_area, is_inside_circle
from solutions.task_02_operations import make_twenty_five
from solutions.task_03_favorite_movies import MY_FAVORITE_MOVIES, pick_movies
from solutions.task_04_my_family import MY_FAMILY_HEIGHT, fathers_height, total_height
from solutions.task_05_zoo import BIRDS, ZOO, cell_number, final_zoo
from solutions.task_06_songs_list import (
    VIOLATOR_SONGS_DICT,
    VIOLATOR_SONGS_LIST,
    total_duration_dict,
    total_duration_list,
)
from solutions.task_07_secret import SECRET_MESSAGE, decode_secret
from solutions.task_08_garden import (
    GARDEN,
    MEADOW,
    all_flowers,
    flowers_in_both,
    flowers_only_in_garden,
    flowers_only_in_meadow,
)
from solutions.task_09_shopping import SWEETS
from solutions.task_10_store import GOODS, STORE, stock_report


def run_all():
    return {
        'distances': build_distances(SITES),
        'circle_area': circle_area(RADIUS),
        'points_inside_circle': (
            is_inside_circle((23, 34)),
            is_inside_circle((30, 30)),
        ),
        'formula_result': make_twenty_five(),
        'movies': pick_movies(MY_FAVORITE_MOVIES),
        'family_heights': (
            fathers_height(MY_FAMILY_HEIGHT),
            total_height(MY_FAMILY_HEIGHT),
        ),
        'zoo': final_zoo(ZOO, BIRDS),
        'songs_durations': (
            total_duration_list(
                VIOLATOR_SONGS_LIST, ('Halo', 'Enjoy the Silence', 'Clean')),
            total_duration_dict(
                VIOLATOR_SONGS_DICT, ('Sweetest Perfection', 'Policy of Truth', 'Blue Dress')),
        ),
        'secret_phrase': decode_secret(SECRET_MESSAGE),
        'flowers': (
            all_flowers(GARDEN, MEADOW),
            flowers_in_both(GARDEN, MEADOW),
            flowers_only_in_garden(GARDEN, MEADOW),
            flowers_only_in_meadow(GARDEN, MEADOW),
        ),
        'sweets': SWEETS,
        'store_report': stock_report(GOODS, STORE),
    }


def print_report(results):
    print(' 00. Расстояния между городами ')
    print(results['distances'])
    print(' 01. Круг ')
    print('Площадь круга:', results['circle_area'])
    print('Точки (23, 34) и (30, 30) внутри круга:', *results['points_inside_circle'])
    print(' 02. Формула ')
    print('Результат:', results['formula_result'])
    print(' 03. Любимые фильмы ')
    print(*results['movies'], sep='\n')
    print(' 04. Семья ')
    height, total = results['family_heights']
    print(f'Рост отца - {height} см, общий рост семьи - {total} см')
    print(' 05. Зоопарк ')
    print(results['zoo'])
    print('lion -', cell_number(results['zoo'], 'lion'), 'клетка')
    print('lark -', cell_number(results['zoo'], 'lark'), 'клетка')
    print(' 06. Песни ')
    print('Три песни звучат', results['songs_durations'][0], 'минут')
    print('А другие три песни звучат', results['songs_durations'][1], 'минут')
    print(' 07. Шифровка ')
    print(results['secret_phrase'])
    print(' 08. Цветы ')
    print('Все виды:', results['flowers'][0])
    print('И там и там:', results['flowers'][1])
    print('Только в саду:', results['flowers'][2])
    print('Только на лугу:', results['flowers'][3])
    print(' 09. Магазины ')
    print(results['sweets'])
    print(' 10. Склад ')
    print(*results['store_report'], sep='\n')


if __name__ == '__main__':
    print_report(run_all())
