__author__ = 'KoicsD'


class PrimeFactors:

    @staticmethod
    def factorize(num):
        if type(num) != int:
            raise TypeError()
