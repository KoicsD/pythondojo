__author__ = 'KoicsD'


# Task: to write a function which decides if a text contains all letters of the alphabet


def init_alphabet():
    alphabet = {}
    for ch in [chr(i) for i in range(ord('a'), ord('z') + 1)]:
        alphabet[ch] = 0
    return alphabet


def count_letters(text, alphabet):
    for ch in text.lower():
        if ch in alphabet:
            alphabet[ch] += 1
    return alphabet


def pangram(text):
    alphabet = init_alphabet()  # alphabet of type dict
    alphabet = count_letters(text, alphabet)  # values of alphabet contains counts
    if 0 in alphabet.values():
        return False
    else:
        return True


if __name__ == "__main__":
    def test_fcn(sample, estres):
        print("for '" + sample + "'(it should be " + str(estres) + "):")
        assert pangram(sample) == estres, "fails"
        print("OK")

    print("testing...")
    test_fcn("ABCDEF", False)
    test_fcn("The quick brown fox jumps over the lazy dog.", True)
    test_fcn("ABC DEF GHI JKL MNO PQRS TUV WXYZ", True)
    print("Code has passed the test!")
