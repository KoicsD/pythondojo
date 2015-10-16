__author__ = 'KoicsD'


def checkio(buildings):
    x_min = min([buildings[i][0] for i in range(len(buildings))])
    x_max = max([buildings[i][2] for i in range(len(buildings))])
    y_min = min([buildings[i][1] for i in range(len(buildings))])
    y_max = max([buildings[i][3] for i in range(len(buildings))])
    visible = set()
    for x in range(x_min, x_max + 1):
        maximum_height = 0
        for y in range(y_min, y_max + 1):
            for building_index in range(len(buildings)):
                if buildings[building_index][0] <= x <= buildings[building_index][2] and\
                        buildings[building_index][1] <= y <= buildings[building_index][3]:
                    if buildings[building_index][4] > maximum_height:
                        maximum_height = buildings[building_index][4]
                        visible.add(building_index)
    return len(visible)


if __name__ == "__main__":
    assert checkio([
        [1, 1, 4, 5, 3.5],
        [2, 6, 4, 8, 5],
        [5, 1, 9, 3, 6],
        [5, 5, 6, 6, 8],
        [7, 4, 10, 6, 4],
        [5, 7, 10, 8, 3]
        ]) == 5, "First"
    assert checkio([
        [1, 1, 11, 2, 2],
        [2, 3, 10, 4, 1],
        [3, 5, 9, 6, 3],
        [4, 7, 8, 8, 2]
        ]) == 2, "Second"
    assert checkio([
        [1, 1, 3, 3, 6],
        [5, 1, 7, 3, 6],
        [9, 1, 11, 3, 6],
        [1, 4, 3, 6, 6],
        [5, 4, 7, 6, 6],
        [9, 4, 11, 6, 6],
        [1, 7, 11, 8, 3.25]
        ]) == 4, "Third"
