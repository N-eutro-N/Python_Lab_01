GARDEN = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

MEADOW = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )


def all_flowers(garden, meadow):
    """Все виды цветов: объединение множеств."""
    return set(garden) | set(meadow)


def flowers_in_both(garden, meadow):
    """Виды, растущие и там и там: пересечение."""
    return set(garden) & set(meadow)


def flowers_only_in_garden(garden, meadow):
    """Виды, растущие только в саду: разность."""
    return set(garden) - set(meadow)


def flowers_only_in_meadow(garden, meadow):
    """Виды, растущие только на лугу: разность."""
    return set(meadow) - set(garden)


if __name__ == '__main__':
    print(all_flowers(GARDEN, MEADOW))
    print(flowers_in_both(GARDEN, MEADOW))
    print(flowers_only_in_garden(GARDEN, MEADOW))
    print(flowers_only_in_meadow(GARDEN, MEADOW))
