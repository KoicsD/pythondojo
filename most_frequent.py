__author__ = 'KoicsD'


def check_if_text_is_in_range(text):
    return 0 < len(text) < 10**5


from pangram import init_alphabet


from pangram import count_letters


def get_lowest_ascii_code(character_array):
    min_code = ord(character_array[0])
    for i in range(1, len(character_array)):
        if ord(character_array[i]) < min_code:
            min_code = ord(character_array[i])
    return chr(min_code)


def checkio(text):
    alphabet = init_alphabet()
    alphabet = count_letters(text, alphabet)
    if len(alphabet.keys()) < 1:
        return None
    most_frequent_chars = []
    max_count = 0
    for key in alphabet.keys():
        if alphabet[key] > max_count:
            max_count = alphabet[key]
            most_frequent_chars = [key]
        elif alphabet[key] == max_count:
            most_frequent_chars.append(key)
    return get_lowest_ascii_code(most_frequent_chars)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
