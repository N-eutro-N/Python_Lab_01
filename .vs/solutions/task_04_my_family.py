MY_FAMILY = ['отец', 'мать', 'сестра', 'дедушка']

MY_FAMILY_HEIGHT = [
    ['отец', 184],
    ['мать', 181],
    ['сестра', 173],
    ['дедушка', 187],
]


def fathers_height(heights):
    i = 0;
    while i < len(heights):
        if heights[i][0] == 'отец':
            return heights[0][1]
        else:
            return("Ничего не нашлось")
        i += 1


def total_height(heights):
    return sum(member[1] for member in heights)


if __name__ == '__main__':
    print(f"Рост отца - {fathers_height(MY_FAMILY_HEIGHT)} см")
    print(f"Общий рост моей семьи - {total_height(MY_FAMILY_HEIGHT)} см")
