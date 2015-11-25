__author__ = 'KoicsD'

import unittest
from string_calculator.string_calc import StringCalc


class MyTestCase(unittest.TestCase):
    def assistant_add_Inp_ReturnsAnsEst(self, inp: str, ans_est: int, msg=None):
        ans = StringCalc.add(inp)
        self.assertEqual(ans, ans_est, msg)

    def test_add_EmptyString_ReturnsZero(self):
        self.assistant_add_Inp_ReturnsAnsEst("", 0)

    def test_add_CommaSeparatedValues_ReturnsSum(self):
        self.assistant_add_Inp_ReturnsAnsEst("1,2,3", 6, "1 + 2 + 3 = 6")

    def test_add_DelimiterChangeable(self):
        self.assistant_add_Inp_ReturnsAnsEst("\\;1;2;3", 6, "',' changed to: ';'")

if __name__ == '__main__':
    unittest.main()
