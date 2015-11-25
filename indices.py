__author__ = 'KoicsD'


DIRECTIONS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


letters = [
    'oiodifnqwoun',
    'gvrosmw;ebgvrpogjep',
    'igonvesljd',
    'iurt422tfcc jhbfv hi00=',
]


def safe_add_to_list(lst: list, row: int, col: int):
    if row in range(len(letters)):
        if col in range(len(letters[row])):
            lst.append(letters[row][col])


def neighbours(row: int, col: int):
    ret = []
    for direction in DIRECTIONS:
        safe_add_to_list(ret, row + direction[0], col + direction[1])
    return ret


if __name__ == "__main__":
    print("first an ordinary example")
    print(2, 3, neighbours(2, 3))
    print("some edge example")
    print(2, 0, neighbours(2, 0))
    print(0, 3, neighbours(0, 3))
    print(2, 9, neighbours(2, 9))
    print("corner")
    print(0, 0, neighbours(0, 0))
    print("out of table")
    print(2, 10, neighbours(2, 10))
