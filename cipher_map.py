__author__ = 'KoicsD'


def rotate_mask(mask):
    s_ret = [['.'] * 4, ['.'] * 4, ['.'] * 4, ['.'] * 4]
    for i in range(4):
        for j in range(4):
            s_ret[i][j] = mask[3-j][i]
    ret = (''.join(s_ret[0]), ''.join(s_ret[1]), ''.join(s_ret[2]), ''.join(s_ret[3]))
    return ret


def recall_password(chipper, cpd_pswd):
    password = ""
    for turn in range(4):
        for i in range(4):
            for j in range(4):
                if chipper[i][j] == 'X':
                    password += cpd_pswd[i][j]
        chipper = rotate_mask(chipper)
    return password


if __name__ == "__main__":
    assert recall_password(
                        ('X...',
                         '..X.',
                         'X..X',
                         '....'),
                        ('itdf',
                         'gdce',
                         'aton',
                         'qrdi')) == 'icantforgetiddqd', "1st example"

    assert recall_password(
                        ('....',
                         'X..X',
                         '.X..',
                         '...X'),
                        ('xhwc',
                         'rsqx',
                         'xqzz',
                         'fyzr')) == 'rxqrwsfzxqxzhczy', "2nd example"