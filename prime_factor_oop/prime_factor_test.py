__author__ = 'KoicsD'


import unittest
from prime_factor_oop.prime_factor import PrimeFactors


class MyTestCase(unittest.TestCase):
    def test_one_returns_empty_list(self):
        self.assertEqual([], PrimeFactors.factorize(1))

    def test_two_returns_two(self):
        self.assertEqual([2], PrimeFactors.factorize(2))

    def test_three_returns_three(self):
        self.assertEqual([3], PrimeFactors.factorize(3))

    def test_four_returns_two_to_two(self):
        self.assertEqual([2, 2], PrimeFactors.factorize(4))

    def test_nine_returns_three_to_two(self):
        self.assertEqual([3, 3], PrimeFactors.factorize(9))

    def test_ten_returns_two_by_five(self):
        self.assertEqual([2, 5], PrimeFactors.factorize(10))

    def test_zero_returns_empty_list(self):
        self.assertEqual([], PrimeFactors.factorize(0))

    def test_minus_four_returns_empty_list(self):
        self.assertEqual([], PrimeFactors(-4))

    def test_twenty_one_returns_three_by_seven(self):
        self.assertEqual()

    def test_twenty_three_returns_twenty_three(self):
        self.assertEqual()


if __name__ == "__main__":
    unittest.main()
