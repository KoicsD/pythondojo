__author__ = 'KoicsD'


def checkio(matrix):
    for j in range(len(matrix)):
        for i in range(len(matrix)):
            if matrix[i][j] != -matrix[j][i]:
                return False
    return True


if __name__ == "__main__":
    assert checkio([
                    [ 0,  1,  2],
                    [-1,  0,  1],
                    [-2, -1,  0]]) == True, "1st example"
    assert checkio([
                    [ 0,  1, 2],
                    [-1,  1, 1],
                    [-2, -1, 0]]) == False, "2nd example"
    assert checkio([
                    [ 0,  1, 2],
                    [-1,  0, 1],
                    [-3, -1, 0]]) == False, "3rd example"
