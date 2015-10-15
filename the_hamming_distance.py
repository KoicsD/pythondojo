__author__ = 'KoicsD'


def checkio(num1, num2):
    str1 = bin(num1)[2:]
    str2 = bin(num2)[2:]
    len1 = len(str1)
    len2 = len(str2)
    diff = len2 - len1
    if diff > 0:  # 2nd longer
        str1 = '0' * diff + str1
    elif diff < 0:  # 1st longer
        str2 = '0' * -diff + str2
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count


"""
def checkio(num1, num2):
    return bin(num1 ^ num2)[2:].count('1')
"""


if __name__ == "__main__":
    assert checkio(117, 17) == 3, "1st example"
    assert checkio(1, 2) == 2, "2nd example"
    assert checkio(16, 15) == 5, "3rd example"
