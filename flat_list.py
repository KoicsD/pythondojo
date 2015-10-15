__author__ = 'KoicsD'


def flat_list(lst):
    result = []
    for item in lst:
        if not isinstance(item, list):
            result += [item]
        else:
            result += flat_list(item)
    return result


def flat_list2(lst):
    list_as_string = str(lst)
    list_as_string = list_as_string[1:-1]
    list_as_string = list_as_string.replace("[","").replace("]","").replace(" ","")
    items = list_as_string.split(",")
    return [int(i) for i in items]


if __name__ == "__main__":
    assert flat_list([1, 2, 3]) == [1, 2, 3], "1st example"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "2nd example"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "3rd example"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "4th example"

    assert flat_list2([1, 2, 3]) == [1, 2, 3], "1st example"
    assert flat_list2([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "2nd example"
    assert flat_list2([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "3rd example"
    assert flat_list2([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "4th example"