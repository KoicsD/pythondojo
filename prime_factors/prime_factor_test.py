__author__ = 'KoicsD'
import unittest
from prime_factor_rec import PrimeFactor


class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual([], PrimeFactor.generate(1))

    def test_two(self):
        self.assertEqual([2], PrimeFactor.generate(2))

    def test_three(self):
        self.assertEqual([3], PrimeFactor.generate(3))

    def test_four(self):
        self.assertEqual([2, 2], PrimeFactor.generate(4))


if __name__ == "__main__":
    unittest.main()