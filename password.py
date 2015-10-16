__author__ = 'KoicsD'


def check_password(password):
    if len(password) < 10:
        return False

    digit = 0
    upper = 0
    lower = 0
    for char in password:
        if char.isdigit():
            digit += 1
        elif char.islower():
            lower += 1
        elif char.isupper():
            upper += 1

    return bool(lower and upper and digit)


if __name__ == "__main__":
    assert check_password("Apok1213pok1") == True, "1st example has not passed"
