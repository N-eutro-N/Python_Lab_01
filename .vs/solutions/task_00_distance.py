SITES = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}


def distance(point_a, point_b):
    """Евклидово расстояние между двумя точками (x, y)."""
    (x_a, y_a), (x_b, y_b) = point_a, point_b
    return ((x_a - x_b) ** 2 + (y_a - y_b) ** 2) ** 0.5


def build_distances(sites):
    return {
        name_a: {
            name_b: distance(coord_a, coord_b)
            for name_b, coord_b in sites.items()
        }
        for name_a, coord_a in sites.items()
    }


if __name__ == '__main__':
    print(build_distances(SITES))
