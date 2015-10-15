__author__ = 'KoicsD'


def quicksort(array):
    if len(array) <= 1:
        return array

    pivot_item = array[0]
    less = []
    equal = []
    greater = []

    for item in array:
        if item < pivot_item:
            less.append(item)
        elif item > pivot_item:
            greater.append(item)
        else:
            equal.append(item)

    return quicksort(less) + equal + quicksort(greater)


if __name__ == "__main__":
    print("Testing...")
    test_array = [5, 8, 9, 3, 4, 6, 1, 2, 3, 9, 8, 5]
    print("for " + str(test_array) + ":")
    output = quicksort(test_array)
    assert output == [1, 2, 3, 3, 4, 5, 5, 6, 8, 8, 9, 9], "error"
    print("OK")
    test_array = [5, 8, 9, 3, 4, 6, 1, 3]
    print("for " + str(test_array) + ":")
    output = quicksort(test_array)
    assert output == [1, 3, 3, 4, 5, 6, 8, 9], "error for " + str(test_array)
    print("OK")
    print("Code is OK!")
