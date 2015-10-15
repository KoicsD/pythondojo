__author__ = 'KoicsD'


# task: count the ones in the binary form of the given number


def check_is_number(value):
    return str(value).isdigit()


def check_number_is_in_range(number):
    return 0 < number <= (2 ** 32)


def binary_count(number):
    if not check_is_number(number):
        return None
    if not check_number_is_in_range(number):
        return None
    binary = bin(number)
    return binary.count('1')
    """
    count = 0
    for c in binary:
        if c == '1':
            count += 1
    return count
    """