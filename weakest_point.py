__author__ = 'KoicsD'


def weak_point(matrix):
    min = sum(matrix[0])
    weakest_row_index = 0
    for row_index in range(1, len(matrix)):
        row_sum = sum(matrix[row_index])
        if row_sum < min:
            min = row_sum
            weakest_row_index = row_index

    min = sum(get_column_by_index(matrix, 0))
    weakest_column_index = 0
    for column_index in range(1, len(matrix[0])):
        column_sum = sum(get_column_by_index(matrix, column_index))
        if column_sum < min:
            min = column_sum
            weakest_column_index = column_index
    return weakest_row_index, weakest_column_index  # [0, 0]


def get_column_by_index(matrix, column_index):
    return [matrix[i][column_index] for i in range(len(matrix))]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"
