__author__ = 'KoicsD'
from sys import argv
from datetime import datetime


# Iterating through the lines of a file
# copying each line to a given other file if the line is palindrom


"""
def is_palindrome(text):
    text_ohne_specchars = filter(lambda c: c.isalnum(), text.lower())
    return text == text[::-1]


print("My name is: " + __name__)
if __name__ == "__main__" and len(argv) == 3:
    with open(argv[1], 'r', encoding="utf-8") as file_in:
        with open(argv[2], 'w', encoding="utf-8") as file_out:
            line = ""
            while True:
                try:
                    line = file_in.readline()
                    if is_palindrome(line):
                        file_out.write(line + '\n')
                except EOFError:
                    break
"""


def is_palindrome(text):
    text_ohne_specchars = [c for c in text.lower() if c.isalnum()]
    return text_ohne_specchars == text_ohne_specchars[::-1]


print("My name is: " + __name__)
if __name__ == "__main__":
    try:
        with open(argv[1], 'r', encoding="utf-8") as file_in:
            with open(argv[2], 'w', encoding="utf-8") as file_out:
                data = file_in.read().splitlines()
                for line in data:
                    if is_palindrome(line):
                        file_out.write(line + '\n')
    except IndexError as ex:
        print("You missed some arguments...Please rerun.")
    except FileNotFoundError as fex:
        print("File Error:")
        print(str(fex))