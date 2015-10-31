__author__ = 'KoicsD'


class IncrementError(Exception):
    pass


class RomanDigit:

    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    signs = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    increase_limits = {1: 2, 5: 3}

    def get_increase_limit(self):
        return RomanDigit.increase_limits[int(str(self.value)[0])]

    def is_possible_increment(self, incr_value: int):
        stringised = str(self.value)
        how_many = int(stringised[0])                                   # unnecessary
        unit = int('1' + stringised[1:])
        assert self.value == how_many * unit, "something went wrong in 'is_possible_increment'"
        return incr_value in [unit, 0]

    def is_possible_decrement(self, decr_value: int):
        stringised = str(self.value)
        how_many = int(stringised[0])
        unit = int('1' + stringised[1:])
        assert self.value == how_many * unit, "something went wrong in 'is_possible_decrement'"
        if how_many == 1:
            return decr_value in [unit // 10, 0]
        elif how_many == 5:
            return decr_value in [unit, 0]

    def __init__(self, data):
        if data == 0 or data == '':
            self.value = 0
            self.sign = ''
        elif type(data) == str:
            if data not in RomanDigit.values:
                raise ValueError("'{0}' is not a valid string for constructing a 'RomanDigit' object".format(data))
            self.sign = data
            self.value = RomanDigit.values[data]
        elif type(data) == int:
            if data not in RomanDigit.signs:
                raise ValueError("{0} is not a valid value for constructing a 'RomanDigit' object".format(data))
            self.value = data
            self.sign = RomanDigit.signs[data]
            assert self.sign == [item for item in RomanDigit.values if RomanDigit.values[item] == data][0],\
                "error in __init__"  # inv(dict[data]) == key
        else:
            raise TypeError("{0} is not a suitable type for constructing a 'RomanDigit' object.".format(type(data)))
        self.increment = None
        self.decrement = None
        self.increase_order = 0

    def increase(self, data, forced=False):
        if type(data) == RomanDigit:
            new_digit = data
        else:
            new_digit = RomanDigit(data)
        if not self.is_possible_increment(new_digit.get_value()):
            raise ValueError("{0} cannot be increased with {1} within the same decimal digit".format(self.sign,
                                                                                                     new_digit.sign))
        if self.decrement is not None:
            if forced:
                self.dispose_decrement()
            else:
                raise IncrementError("{0} cannot be increased without disposing its decrement".format(self.get_sign()))
        if self.increase_order == self.get_increase_limit():
            assert self.increment is not None, "'increment_order' is not 0 but 'increment' is None"     # assert
            raise IncrementError("{0} cannot be further increased".format(self.get_sign()))
        if self.increment is None:
            self.increment = new_digit
        else:
            self.increment.increase(new_digit)
        self.increase_order += 1

    def dispose_increment(self, all_increment=False):
        if all_increment:
            self.increment = None
            self.increase_order = 0
            return
        if self.increment is None:
            assert self.increase_order == 0, "'increment' is None but 'increase_order' is not 0"        # assert
            raise IncrementError("{0} has no increment to dispose".format(self.get_sign()))
        try:
            self.increment.dispose_increment()
        except IncrementError:
            self.increment = None
        assert self.increase_order > 0, "'increment' is not None but 'increase_order' is 0 or less"     # assert
        self.increase_order -= 1

    def decrease(self, data, forced=False):
        if type(data) == RomanDigit:
            new_digit = data
        else:
            new_digit = RomanDigit(data)
        if not self.is_possible_decrement(new_digit.get_value()):
            raise ValueError("{0} cannot be decreased with {1} within the same decimal digit".format(self.sign,
                                                                                                     new_digit.sign))
        if self.increase_order > 0:
            assert self.increment is not None, "'increment_order' is not 0 but 'increment' is None"     # assert
            if forced:
                self.dispose_increment()
            else:
                raise IncrementError("{0} cannot be decreased without disposing its increment".format(self.get_sign()))
        if self.decrement is not None:
            raise IncrementError("{0} cannot be further decreased".format(self.get_sign()))
        self.decrement = new_digit

    def dispose_decrement(self):
        if self.decrement is None:
            raise IncrementError("{0} has no decrement to dispose".format(self.get_sign()))
        self.decrement = None

    def get_value(self):
        ret = self.value
        if self.decrement is not None:
            ret -= self.decrement.get_value()
        elif self.increment is not None:
            ret += self.increment.get_value()
        return ret

    def get_sign(self):
        ret = self.sign
        if self.decrement is not None:
            ret = self.decrement.get_sign() + ret
        elif self.increment is not None:
            ret += self.increment.get_sign()
        return ret


class DecimalDigit:
    pass


class RomanNumeral:
    pass


def main(*args):
    # script-body comes here
    pass

if __name__ == "__main__":
    from sys import argv
    main(*argv)
