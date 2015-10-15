__author__ = 'KoicsD'


# let's name zero:          # zero                      # zero                      # zero
Z = "zero"

# numbers from 1 to 12:     # 1 - 12                    # 1 - 12                    # 1 - 12
n12 = {1: "one",
       2: "two",
       3: "three",
       4: "four",
       5: "five",
       6: "six",
       7: "seven",
       8: "eight",
       9: "nine",
       10: "ten",
       11: "eleven",
       12: "twelve"}


# from 0 to 20:             # 0 - 20                    # 0 - 20                    # 0 -20
def to20(num):
    # Names the integers from 0 to 20 (both including).
    # Uses the name 'Z' and the dict 'n12'.

    # only for int in range 0 - 20 (both including)
    if type(num) != int or not 0 <= num <= 20:
        print("Para in 'to20'!")
        return None

    if num == 0:  # 0 has a separate name
        return Z
    elif num <= 12:  # 1 - 12 in dict
        return n12[num]
    elif num < 20:  # 13 - 20 is a bit more difficult
        nones = num % 10  # number of ones
        # like 3 - 9 but with ending -'teen', except 3, 5, and 8:
        if nones == 3:
            return "thirteen"
        elif nones == 5:
            return "fifteen"
        elif nones == 8:
            return "eighteen"
        else:
            return n12[nones] + "teen"
    else:  # num == 20
        return "twenty"


# from 0 to 100:            # 0 - 100                   # 0 - 100                   # 0 - 100
def to100(num):
    # Names the integers from 0 to 100 (both including).
    # Uses the function 'to20' and the dict 'n12'
    #   (Function 'to20' uses the name 'Z' as well)

    # only for int in range 0 - 100 (both including)
    if type(num) != int or not 0 <= num <= 100:
        print("Para in fun 'to100'!")
        return None

    if num <= 20:  # 0 - 20 solved by fun 'to20'
        return to20(num)
    elif num < 100:  # 21 - 100 is a bit more difficult
        ntens = (num % 100) // 10  # number of tens
        nones = num % 10  # number of ones
        # 20, 30 .. 90 like 2, 3 .. 9 but with ending -'ty', except 20, 30, 40 and 50:
        if ntens == 2:
            stens = "twenty"
        elif ntens == 3:
            stens = "thirty"
        elif ntens == 4:
            stens = "forty"
        elif ntens == 5:
            stens = "fifty"
        elif ntens == 8:
            stens = "eighty"
        else:
            stens = n12[ntens] + "ty"
        if nones == 0:  # if no ones, return simply the name 20, 30, .. 90
            return stens
        else:  # otherwise ones are coupled with '-':
            return stens + "-" + n12[nones]
    else:  # num == 100
        return "one hundred"


# from 0 to 1000:           # 0 - 1000                  # 0 - 1000                  # 0 - 1000
def to1000(num):
    # Names the numbers for 0 to 1000 (both including).
    # Uses the function 'to100' and the dict 'n12'.
    #   (The name 'Z' is also used implicitly.)

    # only for int in range 0 - 1000 (both including):
    if type(num) != int or not 0 <= num <= 1000:
        print("Para in fun 'to1000'!")
        return None

    if num <= 100:  # 0 - 100 solved by fun 'to100'
        return to100(num)
    elif num < 1000:  # 101 - 1000 is a bit more difficult
        nhunds = (num % 1000) // 100  # number of hundreds
        nto100 = num % 100  # number of tens_and_ones
        if nto100 == 0:  # if no tens_and_ones, simply name hundreds
            return n12[nhunds] + " hundred"
        else:  # otherwise tens_and_ones are coupled with ' and '
            return n12[nhunds] + " hundred and " + to100(nto100)
    else:  # num == 1000
        return "one thousand"


# main converter function:                              # -1000 - 1000          # -1000 - 1000
def num2str(num, toprint=False):
    # Names the integers from -1000 to +1000.
    # It uses function 'to1000' and dict 'n12' explicitly,
    #   but the name 'Z' is also used implicitly.

    # only for int in range -1000 - 1000 (both including)
    if type(num) != int or not -1000 <= num <= 1000:
        print("Para in fun 'num2str'!")
        return None

    if num < 0:  # -1 .. -1000 is like 1 .. 1000 but with prefix 'minus '-
        ret = "minus " + to1000(-num)
    else:  # 0 .. 1000 is solved by fun 'to1000'
        ret = to1000(num)
    if toprint:  # if user wanna print, let's do it
        print(ret)
    return ret


#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
if __name__ == "__main__":  # test-script

    # test-function:
    def test(num, est):
        print("testing for: " + str(num))
        print("\tit should be: '" + est + "'")
        got = num2str(num)
        print("\tit is: '" + got + "'")
        assert got == est, "Failure"
        print("\tOK")

    # trying different values:
    print("Let's test our function!")
    test(0, "zero")
    test(5, "five")
    test(12, "twelve")
    test(15, "fifteen")
    test(18, "eighteen")
    test(20, "twenty")
    test(23, "twenty-three")
    test(30, "thirty")
    test(36, "thirty-six")
    test(40, "forty")
    test(45, "forty-five")
    test(50, "fifty")
    test(55, "fifty-five")
    test(60, "sixty")
    test(65, "sixty-five")
    test(100, "one hundred")
    test(105, "one hundred and five")
    test(112, "one hundred and twelve")
    test(115, "one hundred and fifteen")
    test(118, "one hundred and eighteen")
    test(120, "one hundred and twenty")
    test(123, "one hundred and twenty-three")
    test(130, "one hundred and thirty")
    test(136, "one hundred and thirty-six")
    test(140, "one hundred and forty")
    test(145, "one hundred and forty-five")
    test(150, "one hundred and fifty")
    test(155, "one hundred and fifty-five")
    test(160, "one hundred and sixty")
    test(165, "one hundred and sixty-five")
    test(300, "three hundred")
    test(305, "three hundred and five")
    test(312, "three hundred and twelve")
    test(315, "three hundred and fifteen")
    test(318, "three hundred and eighteen")
    test(320, "three hundred and twenty")
    test(323, "three hundred and twenty-three")
    test(330, "three hundred and thirty")
    test(336, "three hundred and thirty-six")
    test(340, "three hundred and forty")
    test(345, "three hundred and forty-five")
    test(350, "three hundred and fifty")
    test(355, "three hundred and fifty-five")
    test(360, "three hundred and sixty")
    test(365, "three hundred and sixty-five")
    test(1000, "one thousand")
    test(-5, "minus five")
    test(-12, "minus twelve")
    test(-15, "minus fifteen")
    test(-18, "minus eighteen")
    test(-20, "minus twenty")
    test(-23, "minus twenty-three")
    test(-30, "minus thirty")
    test(-36, "minus thirty-six")
    test(-40, "minus forty")
    test(-45, "minus forty-five")
    test(-50, "minus fifty")
    test(-55, "minus fifty-five")
    test(-60, "minus sixty")
    test(-65, "minus sixty-five")
    test(-100, "minus one hundred")
    test(-105, "minus one hundred and five")
    test(-112, "minus one hundred and twelve")
    test(-115, "minus one hundred and fifteen")
    test(-118, "minus one hundred and eighteen")
    test(-120, "minus one hundred and twenty")
    test(-123, "minus one hundred and twenty-three")
    test(-130, "minus one hundred and thirty")
    test(-136, "minus one hundred and thirty-six")
    test(-140, "minus one hundred and forty")
    test(-145, "minus one hundred and forty-five")
    test(-150, "minus one hundred and fifty")
    test(-155, "minus one hundred and fifty-five")
    test(-160, "minus one hundred and sixty")
    test(-165, "minus one hundred and sixty-five")
    test(-300, "minus three hundred")
    test(-305, "minus three hundred and five")
    test(-312, "minus three hundred and twelve")
    test(-315, "minus three hundred and fifteen")
    test(-318, "minus three hundred and eighteen")
    test(-320, "minus three hundred and twenty")
    test(-323, "minus three hundred and twenty-three")
    test(-330, "minus three hundred and thirty")
    test(-336, "minus three hundred and thirty-six")
    test(-340, "minus three hundred and forty")
    test(-345, "minus three hundred and forty-five")
    test(-350, "minus three hundred and fifty")
    test(-355, "minus three hundred and fifty-five")
    test(-360, "minus three hundred and sixty")
    test(-365, "minus three hundred and sixty-five")
    test(-1000, "minus one thousand")
    print("Test All Right!")
