__author__ = 'KoicsD'

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 != 0:
        return "Fizz"
    elif number % 3 != 0 and number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    else:
        return str(number)

if __name__ == '__main__':
    assert fizz_buzz(7) == "7", "7 is not divisible by 3 or 5"
    assert fizz_buzz(6) == "Fizz", "6 is divisible by 3"
    assert fizz_buzz(5) == "Buzz", "5 is divisible by 5"
    assert fizz_buzz(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    print("Code is OK")