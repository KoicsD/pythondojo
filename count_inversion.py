__author__ = 'KoicsD'


def check_if_length_is_valid(values):
    if not 2 < len(values) < 200:
        return False
    else:
        return True


def check_if_values_are_in_range(values):
    for value in values:
        if not -100 < value < 100:
            return False
    return True


def count_lowers(values, index):
    count = 0
    for ind in range(index + 1, len(values)):
        if values[index] > values[ind]:
            count += 1
    return count


def count_inversion(values):
    if not check_if_length_is_valid(values):
        print("Length of list must be between 2 and 100!")
        return None
    if not check_if_values_are_in_range(values):
        print("Values must be between -100 and +100!")
        return None
    count = 0
    for index in range(len(values)-1):
        count += count_lowers(values, index)
    return count


if __name__ == "__main__":
    assert count_inversion((0, 1, 2, 3, 4)) == 0, "count_inversion must return 0 for (0, 1, 2, 3, 4)!"
    assert count_inversion((0, 1, 3, 2, 4)) == 1, "count_inversion must return 1 for (0, 1, 3, 2, 4)!"
    assert count_inversion((1, 2, 5, 6, 4, 7, 6)) == 3, "count_inversion must return 3 for (1, 2, 5, 6, 4, 7, 6)!"
    assert count_inversion([i for i in range(300)]) is None, "count_inversion must not work for a 300-element list!"
    print("Code is OK!")
    assert 0 == 0, "mijjafasz???!!! zero is not zero?!"
    print("System is OK!")
