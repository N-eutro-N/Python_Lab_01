RADIUS = 42
PI = 3.1415926


def circle_area(radius, pi=PI):
    return round(pi * radius ** 2, 4)


def is_inside_circle(point, radius=RADIUS):
    x, y = point
    return (x ** 2 + y ** 2) ** 0.5 <= radius


if __name__ == '__main__':
    print(circle_area(RADIUS))
    print(is_inside_circle((23, 34)))
    print(is_inside_circle((30, 30)))
