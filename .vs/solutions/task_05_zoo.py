ZOO = ['lion', 'kangaroo', 'elephant', 'monkey']
BIRDS = ['rooster', 'ostrich', 'lark']


def append_birds(zoo, birds):
    """Птицы в последние клетки."""
    result = list(zoo)
    result.extend(birds)
    return result


def remove_animal(zoo, animal):
    """Убирает животное из зоопарка."""
    result = list(zoo)
    result.remove(animal)
    return result


def cell_number(zoo, animal):
    """Номер клетки животного, счёт с 1."""
    return zoo.index(animal) + 1

def place_animal_after(zoo, animal, afterWho):
    """Медведь между львом и кенгуру."""
    result = list(zoo)
    place = cell_number(zoo, afterWho)
    result.insert(place + 1, animal)
    return result

def final_zoo(zoo=ZOO, birds=BIRDS):
    return remove_animal(append_birds(place_animal_after(zoo, 'bear', 'lion'), birds), 'elephant')


if __name__ == '__main__':
    print(place_animal_after(ZOO, 'bear', 'lion'))
    print(append_birds(place_animal_after(ZOO, 'bear', 'lion'), BIRDS))
    print(final_zoo())
    print('lion -', cell_number(final_zoo(), 'lion'), 'клетка')
    print('lark -', cell_number(final_zoo(), 'lark'), 'клетка')
