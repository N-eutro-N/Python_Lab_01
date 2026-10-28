import pytest

import lab
from solutions.task_00_distance import SITES, build_distances, distance
from solutions.task_01_circle import RADIUS, circle_area, is_inside_circle
from solutions.task_02_operations import make_twenty_five
from solutions.task_03_favorite_movies import MY_FAVORITE_MOVIES, pick_movies
from solutions.task_04_my_family import (
    MY_FAMILY_HEIGHT,
    fathers_height,
    total_height,
)
from solutions.task_05_zoo import (
    BIRDS,
    ZOO,
    append_birds,
    cell_number,
    final_zoo,
    place_animal_after,
    remove_animal,
)
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
from solutions.task_09_shopping import SHOPS, SWEETS, two_cheapest
from solutions.task_10_store import GOODS, STORE, stock_report


class TestDistance:
    def test_known_pair(self):
        assert distance((550, 370), (510, 510)) == pytest.approx(145.60219778561037)

    def test_diagonal_is_zero(self):
        distances = build_distances(SITES)
        assert all(distances[city][city] == 0 for city in SITES)

    def test_matrix_symmetric(self):
        distances = build_distances(SITES)
        for a in SITES:
            for b in SITES:
                assert distances[a][b] == pytest.approx(distances[b][a])

    def test_matrix_keys(self):
        distances = build_distances(SITES)
        assert set(distances) == set(SITES)
        assert all(set(row) == set(SITES) for row in distances.values())


class TestCircle:
    def test_area(self):
        assert circle_area(RADIUS) == pytest.approx(5541.7693)

    def test_point_inside(self):
        assert is_inside_circle((23, 34)) is True

    def test_point_outside(self):
        assert is_inside_circle((30, 30)) is False

    def test_point_on_border_counts_as_inside(self):
        assert is_inside_circle((42, 0)) is True


class TestOperations:
    def test_result_is_25(self):
        assert make_twenty_five() == 25


class TestMovies:
    def test_pick_order(self):
        assert pick_movies(MY_FAVORITE_MOVIES) == (
            'Терминатор',
            'Назад в будущее',
            'Пятый элемент',
            'Чужие',
        )

    def test_no_commas_in_titles(self):
        assert all(',' not in movie for movie in pick_movies(MY_FAVORITE_MOVIES))


class TestFamily:
    def test_fathers_height(self):
        assert fathers_height(MY_FAMILY_HEIGHT) == 184

    def test_total_height(self):
        assert total_height(MY_FAMILY_HEIGHT) == 725

    def test_total_height_custom_data(self):
        assert total_height([['a', 100], ['b', 50], ['c', 25]]) == 175


class TestZoo:
    def test_bear_between_lion_and_kangaroo(self):
        zoo = place_animal_after(ZOO, 'bear', 'lion')
        assert zoo[:3] == ['lion', 'bear', 'kangaroo']

    def test_birds_appended_to_end(self):
        assert append_birds(ZOO, BIRDS)[-3:] == BIRDS

    def test_elephant_removed(self):
        assert 'elephant' not in remove_animal(ZOO, 'elephant')

    def test_final_zoo(self):
        assert final_zoo() == [
            'lion', 'bear', 'kangaroo', 'monkey', 'rooster', 'ostrich', 'lark',
        ]

    def test_cell_numbers_are_one_indexed(self):
        zoo = final_zoo()
        assert cell_number(zoo, 'lion') == 1
        assert cell_number(zoo, 'lark') == 7

    def test_source_list_not_mutated(self):
        place_animal_after(ZOO, 'bear', 'lion')
        append_birds(ZOO, BIRDS)
        remove_animal(ZOO, 'elephant')
        assert ZOO == ['lion', 'kangaroo', 'elephant', 'monkey']


class TestSongs:
    def test_list_total(self):
        total = total_duration_list(
            VIOLATOR_SONGS_LIST, ('Halo', 'Enjoy the Silence', 'Clean'))
        assert total == pytest.approx(14.93)

    def test_dict_total(self):
        total = total_duration_dict(
            VIOLATOR_SONGS_DICT, ('Sweetest Perfection', 'Policy of Truth', 'Blue Dress'))
        assert total == pytest.approx(13.49)

    def test_rounding_of_float_sum(self):
        assert total_duration_dict({'a': 0.1, 'b': 0.2}, ('a', 'b')) == pytest.approx(0.3)


class TestSecret:
    def test_decoded_phrase(self):
        assert decode_secret(SECRET_MESSAGE) == 'в бане веник дороже денег'

    def test_phrase_has_five_words(self):
        assert len(decode_secret(SECRET_MESSAGE).split()) == 5


class TestGarden:
    def test_all_kinds(self):
        assert all_flowers(GARDEN, MEADOW) == {
            'ромашка', 'одуванчик', 'роза', 'гладиолус', 'подсолнух', 'клевер', 'мак',
        }

    def test_in_both(self):
        assert flowers_in_both(GARDEN, MEADOW) == {'ромашка', 'одуванчик'}

    def test_only_in_garden(self):
        assert flowers_only_in_garden(GARDEN, MEADOW) == {'роза', 'гладиолус', 'подсолнух'}

    def test_only_in_meadow(self):
        assert flowers_only_in_meadow(GARDEN, MEADOW) == {'клевер', 'мак'}


class TestShopping:
    def test_sweets_matches_two_cheapest(self):
        for product, offers in SWEETS.items():
            assert offers == two_cheapest(SHOPS, product)

    def test_each_product_has_two_sorted_offers(self):
        for offers in SWEETS.values():
            assert len(offers) == 2
            assert offers[0]['price'] <= offers[1]['price']


class TestStore:
    def test_report_lines(self):
        assert stock_report(GOODS, STORE) == [
            'Лампа - 27 шт, стоимость 1134 руб',
            'Стол - 54 шт, стоимость 27860 руб',
            'Диван - 3 шт, стоимость 3550 руб',
            'Стул - 105 шт, стоимость 10311 руб',
        ]


class TestLab:
    EXPECTED_KEYS = {
        'distances', 'circle_area', 'points_inside_circle', 'formula_result',
        'movies', 'family_heights', 'zoo', 'songs_durations',
        'secret_phrase', 'flowers', 'sweets', 'store_report',
    }

    def test_run_all_returns_all_sections(self):
        assert set(lab.run_all()) == self.EXPECTED_KEYS

    def test_run_all_is_deterministic(self):
        assert lab.run_all() == lab.run_all()

    def test_print_report_output(self, capsys):
        lab.print_report(lab.run_all())
        output = capsys.readouterr().out
        assert 'в бане веник дороже денег' in output
        assert 'Три песни звучат 14.93 минут' in output
        assert 'Лампа - 27 шт, стоимость 1134 руб' in output
        assert 'Площадь круга: 5541.7693' in output
