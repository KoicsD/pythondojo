__author__ = 'Zsori Lukacs Peter'

def check_if_text_lenght_is_in_range(text):
    return 0 < len(text) < 10**5


def initialize_dictionary(sentence):
    lower_sentence = sentence.lower()
    text = {}
    for c in lower_sentence:
        if c.isalpha():
            if c in text.keys():
                text[c] += 1
            else:
                text[c] = 1
    return text

def get_lowest_ascii_code(character_array):
    min_code = ord(character_array[0])
    for i in range(1,len(character_array)):  # hey, indexing starts with zero!
         if ord(character_array[i]) < min_code:
            min_code = ord(character_array[i])
    return chr(min_code)

def checkio(text):
    dict = initialize_dictionary(text)
    if len(dict.keys()) < 1:
        return None
    most_frequent_chars = []
    max_count = 0
    for key in dict.keys():
        if dict[key] > max_count:
            max_count = dict[key]
            most_frequent_chars = [key]
        elif dict[key] == max_count:
            most_frequent_chars.append(key)
        # if len(most_frequent_chars) > 1:
        #     return get_lowest_ascii_code  # return in for???

    if len(most_frequent_chars) > 1:
        return get_lowest_ascii_code(most_frequent_chars)

    return most_frequent_chars[0]


#print(checkio("One one appl"))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def test(inp, outp, msg):
        print(msg)
        print("Input: " + inp)
        print("Output, what it should be: " + outp)
        ret = checkio(inp)
        print("Output, what it is: " + ret)
        assert outp == ret, msg
        print("OK")

    test("Hello World!","l", "Hello test")
    test("How do you do?", "o", "O is most wanted")
    test("One", "e", "All letter only once.")
    test("Oops!", "o", "Don't forget about lower case.")
    test("AAaooo!!!!","a", "Only letters.")
    test("abe", "a", "The First.")
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")