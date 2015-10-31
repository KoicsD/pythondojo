__author__ = 'KoicsD'

import unittest
import roman_numerals as my_module

class MyTestCase(unittest.TestCase):
    values = [1, 5, 10, 50, 100, 500, 1000]
    signs = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    increment_values = [1, 1, 10, 10, 100, 100, 1000]
    increment_signs = ['I', 'I', 'X', 'X', 'C', 'C', 'M']
    max_increment_nums = [2, 3, 2, 3, 2, 3, 2]
    decrement_values = [0, 1, 1, 10, 10, 100, 100]
    decrement_signs = ['', 'I', 'I', 'X', 'X', 'C', 'C']

    def test_RomanDigit_TypeError_for_float(self):

        self.assertRaises(TypeError, my_module.RomanDigit, 5.5)

    def test_RomanDigit_ValueError_for_wrong_int(self):
        self.assertRaises(ValueError, my_module.RomanDigit, 6)

    def test_RomanDigit_ValueError_for_wrong_letter(self):
        self.assertRaises(ValueError, my_module.RomanDigit, 'S')

    def test_RomanDigit_for_int(self):
        # tests if all RomanDigits can be constructed from it's value
        # also tests if these digits knows their own increase-limits
        for i in range(len(MyTestCase.values)):
            v = MyTestCase.values[i]
            s = MyTestCase.signs[i]
            my_obj = my_module.RomanDigit(v)
            self.assertEqual(my_obj.get_value(), v, 'value is not all-right (value: {0}, sign: {1})'.format(v, s))
            self.assertEqual(my_obj.get_sign(), s, 'sign is not all-right (value: {0}, sign: {1})'.format(v, s))
            self.assertEqual(my_obj.get_increase_limit(), MyTestCase.max_increment_nums[i],
                             'sign is not all-right (value: {0}, sign: {1})'.format(v, s))

    def test_RomanDigit_for_str(self):
        # tests if all RomanDigits can be constructed from it's sign
        # also tests if these digits knows their own increase-limits
        for i in range(len(MyTestCase.signs)):
            v = MyTestCase.values[i]
            s = MyTestCase.signs[i]
            my_obj = my_module.RomanDigit(s)
            self.assertEqual(my_obj.get_value(), v, 'value is not all-right (value: {0}, sign: {1})'.format(v, s))
            self.assertEqual(my_obj.get_sign(), s, 'sign is not all-right (value: {0}, sign: {1})'.format(v, s))
            self.assertEqual(my_obj.get_increase_limit(), MyTestCase.max_increment_nums[i],
                             'sign is not all-right (value: {0}, sign: {1})'.format(v, s))

    def test_RomanDigit_increment(self):
        # Tests all the increaser and decreaser functions of RomanDigits.
        # Covers all the 'round' numbers.
        # Checks errors that should be raised when trying to do something impossible or suspicious.

        for i in range(7):
            # initializing base value:
            base_value = MyTestCase.values[i]
            base_sign = MyTestCase.signs[i]
            my_obj = my_module.RomanDigit(base_value)
            v = base_value
            s = base_sign

            # initializing increaser-test:
            increment_value = MyTestCase.increment_values[i]
            increment_sign = MyTestCase.increment_signs[i]
            max_n_increments = MyTestCase.max_increment_nums[i]

            msg = "'V' |--> 'VI' |--> 'VII' |--> 'VIII' ie. 'X' |--> 'XX' |--> 'XXX' etc."
            [my_obj, v, s] = self.increase(base_value, base_sign,
                                           my_obj, v, s,
                                           increment_value, increment_sign, False, max_n_increments, msg)

            msg = "'VIII' |--> 'VIIII' ie. 'XXX' |--> 'XXXX' etc. impossible"
            [my_obj, v, s] = self.increase(base_value, base_sign,
                                           my_obj, v, s,
                                           increment_value, increment_sign, False, 0, msg)
            msg = "'VIII' |--> 'VIIII' ie. 'XXX' |--> 'XXXX' etc. impossible even with forced increase"
            [my_obj, v, s] = self.increase(base_value, base_sign,
                                           my_obj, v, s,
                                           increment_value, increment_sign, True, 0, msg)

            msg = "discarding last increment ('VIII' |--> 'VI' ie. 'XXX' |--> 'XX' etc.)"
            [my_obj, v, s] = self.dispose_increment(base_value, base_sign,
                                                    my_obj, v, s,
                                                    increment_value, increment_sign, False, True, msg)

            msg = "one increment again ('VII' |--> 'VIII' ie. 'XX' |--> 'XXX' etc.)"
            [my_obj, v, s] = self.increase(base_value, base_sign,
                                           my_obj, v, s,
                                           increment_value, increment_sign, False, 1, msg)

            msg = "discarding all increments ('VIII' |--> 'V' ie. 'XXX' |--> 'X' etc.)"
            [my_obj, v, s] = self.dispose_increment(base_value, base_sign,
                                                    my_obj, v, s,
                                                    increment_value, increment_sign, True, True, msg)

            msg = "'V' |--> ... |--> 'VIII' ie. 'X' |--> ... |--> 'XXX' etc. again"
            [my_obj, v, s] = self.increase(base_value, base_sign,
                                           my_obj, v, s,
                                           increment_value, increment_sign, False, max_n_increments, msg)

            msg = "discarding all increments again ('VIII' |--> 'V' ie. 'XXX' |--> 'X' etc.)"
            [my_obj, v, s] = self.dispose_increment(base_value, base_sign,
                                                    my_obj, v, s,
                                                    increment_value, increment_sign, True, True, msg)

            msg = "testing forced increment('V' |--> ... |--> 'VIII' ie. 'X' |--> ... |--> 'XXX' etc. again)"
            [my_obj, v, s] = self.increase(base_value, base_sign,
                                           my_obj, v, s,
                                           increment_value, increment_sign, True, max_n_increments, msg)

            # initializing decreaser-test:
            decrement_value = MyTestCase.decrement_values[i]
            decrement_sign = MyTestCase.decrement_signs[i]

            msg = "'VIII' |--> 'IV' ie. 'XXX' |--> 'IX' etc. directly impossible"
            [my_obj, v, s] = self.decrease(base_value, base_sign,
                                           my_obj, v, s,
                                           decrement_value, decrement_sign, False, False, msg)

            msg = "'VIII' |--> 'IV' ie. 'XXX' |--> 'IX' etc. directly yet possible with forced decreasing"
            [my_obj, v, s] = self.dispose_decrement(base_value, base_sign,
                                                    my_obj, v, s,
                                                    decrement_value, decrement_sign, True, msg)

            msg = "'IV' |--> 'IIV' ie. 'IX' |--> 'IIX' etc. impossible"
            [my_obj, v, s] = self.decrease(base_value, base_sign,
                                           my_obj, v, s,
                                           decrement_value, decrement_sign, False, False, msg)
            msg = "'IV' |--> 'IIV' ie. 'IX' |--> 'IIX' etc. impossible even if forced"
            [my_obj, v, s] = self.decrease(base_value, base_sign,
                                           my_obj, v, s,
                                           decrement_value, decrement_sign, True, False, msg)

            msg = "discarding decrement ('IV' |--> 'V' ie. 'IX' |--> 'X')"
            [my_obj, v, s] = self.dispose_decrement(base_value, base_sign,
                                                    my_obj, v, s,
                                                    decrement_value, decrement_sign, True, msg)

            msg = "'V' |--> 'IV' ie. 'X' |--> 'IX'"
            [my_obj, v, s] = self.decrease(base_value, base_sign,
                                           my_obj, v, s,
                                           decrement_value, decrement_sign, False, True, msg)

            msg = "discarding decrement ('IV' |--> 'V' ie. 'IX' |--> 'X') again"
            [my_obj, v, s] = self.dispose_decrement(base_value, base_sign,
                                                    my_obj, v, s,
                                                    decrement_value, decrement_sign, True, msg)

            msg = "testing forced decrement ('V' |--> 'IV' ie. 'X' |--> 'IX' again)"
            [my_obj, v, s] = self.decrease(base_value, base_sign,
                                           my_obj, v, s,
                                           decrement_value, decrement_sign, True, True, msg)

            # switching back to increasing:

            msg = "'IV' |--> 'VI' ie. 'IX' |--> 'XX' directly impossible"
            [my_obj, v, s] = self.increase(base_value, base_sign,
                                           my_obj, v, s,
                                           increment_value, increment_sign, False, 0, msg)

            msg = "'IV' |--> 'VI' ie. 'IX' |--> 'XX' directly yet possible with forced increase"
            [my_obj, v, s] = self.increase(base_value, base_sign,
                                           my_obj, v, s,
                                           increment_value, increment_sign, True, 1, msg)

    def increase(self, base_val: int, base_sign: str,
                  base_obj: my_module.RomanDigit, v: int, s: str,
                  incr_val: int, incr_sign: str, forced: bool, max_n_incr: int, msg: str):
        # base_val: the base value of the RomanDigit being tested
        # base_sign: the base sign of the RomanDigit being tested
        # base_obj: the RomanDigit to be tested
        # v: the value for incrementing, varies through the loop
        # s: the sign for incrementing, varies through the loop
        # incr_val: the value for calling the increaser function
        # incr_sign: the sign for calling the increaser function
        # forced: decides whether to use forced increment
        # max_n_incr: the number of increments -- failure is asserted if zero
        # msg: message to be displayed on assertion failure
        #
        # return values: the RomanDigit and the value and sign after the test

        if max_n_incr == 0:
            self.assertRaises(my_module.IncrementError, my_module.RomanDigit.increase, base_obj, incr_val, forced)
        for j in range(max_n_incr):
            v += incr_val
            s += incr_sign
            base_obj.increase(incr_val, forced)
            self.assertEqual(base_obj.get_value(), v,
                             'value is not all-right (value: {0}, sign: {1})\nmessage: %s'.format(v, s) % msg)
            self.assertEqual(base_obj.get_sign(), s,
                             'sign is not all-right (value: {0}, sign: {1})\nmessage: %s'.format(v, s) % msg)
        return [base_obj, v, s]

    def dispose_increment(self, base_val: int, base_sign: str,
                          base_obj: my_module.RomanDigit, v: int, s: str,
                          incr_val: int, incr_sign: str, all_increments: bool, assert_success: bool, msg: str):
        # base_val: the base value of the RomanDigit being tested
        # base_sign: the base sign of the RomanDigit being tested
        # base_obj: the RomanDigit to be tested
        # v: the value for incrementing, varies through the loop
        # s: the sign for incrementing, varies through the loop
        # all_increments: decides whether to dispose all increments
        # assert_success: decides whether to assert success
        # msg: message to be displayed on assertion failure
        #
        # return value: the RomanDigit and the value and sign after the test

        if assert_success:
            if all_increments:
                v = base_val
                s = s[1]
            else:
                v -= incr_val
                s = s[:-1]
            base_obj.dispose_increment(all_increments)
            self.assertEqual(base_obj.get_value(), v,
                             'value is not all-right (value: {0}, sign: {1})\nmessage: %s'.format(v, s) % msg)
            self.assertEqual(base_obj.get_sign(), s,
                             'sign is not all-right (value: {0}, sign: {1})\nmessage: %s'.format(v, s) % msg)
        else:
            self.assertRaises(my_module.IncreaseError, my_module.RomanDigit.dispose_increment, base_obj, all_increments)
        return [base_obj, v, s]

    def decrease(self, base_val: int, base_sign: str,
                  base_obj: my_module.RomanDigit, v: int, s: str,
                  decr_val: int, decr_sign: str, forced: bool, assert_success: bool, msg: str):
        # base_val: the base value of the RomanDigit being tested
        # base_sign: the base sign of the RomanDigit being tested
        # base_obj: the RomanDigit to be tested
        # v: the value for decrementing, varies through the loop
        # s: the sign for decrementing, varies through the loop
        # decr_val: the value for calling the decreaser function
        # decr_sign: the sign for calling the decreaser function
        # forced: decides whether to use forced decrement
        # assert_success: decides whether to assert success
        #
        # return values: the RomanDigit and the value and sign after the test

        if assert_success:
            v -= decr_val
            s = decr_sign + s
            base_obj.decrease(decr_val, forced)
            self.assertEqual(base_obj.get_value(), v, 'bla')
            self.assertEqual(base_obj.get_sign(), s, 'bla')
        else:
            self.assertRaises(my_module.IncreaseError, my_module.RomanDigit.decrease, base_obj, decr_val)
        return [base_obj, v, s]

    def dispose_decrement(self, base_val: int, base_sign: str,
                  base_obj: my_module.RomanDigit, v: int, s: str,
                  decr_val: int, decr_sign: str, assert_success: bool, msg: str):
        # base_val: the base value of the RomanDigit being tested
        # base_sign: the base sign of the RomanDigit being tested
        # base_obj: the RomanDigit to be tested
        # v: the value for decrementing, varies through the loop
        # s: the sign for decrementing, varies through the loop
        # decr_val: the value for calling the decreaser function
        # decr_sign: the sign for calling the decreaser function
        # forced: decides whether to use forced decrement
        # assert_success: decides whether to assert success
        #
        # return values: the RomanDigit and the value and sign after the test

        if assert_success:
            v += decr_val
            assert v == base_val and s[-1] == s[1:], "something went wrong with test\nmessage: %s" % msg
            s = s[1:]
            base_obj.dispose_decrement()
            self.assertEqual(base_obj.get_value(), v, 'value is not all-right\nmessage: %s' % msg)
            self.assertEqual(base_obj.get_sign(), s, 'sign is not all-right\nmessage: %s' % msg)
        else:
            self.assertRaises(my_module.IncreaseError, my_module.RomanDigit.dispose_decrement, base_obj)
        return [base_obj, v, s]


if __name__ == '__main__':
    unittest.main()
