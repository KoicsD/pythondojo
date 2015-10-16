__author__ = 'KoicsD'


class PrimeFactor():
    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def generate(n):
        primes = []
        if n > 1:
            if PrimeFactor.is_prime(n):
                return [n]
            primes_to_check = [j for j in range(2, int(n ** 0.5) + 1) if PrimeFactor.is_prime(j)]
            for i in primes_to_check:
                while n % i == 0:
                    primes.append(i)
                    n //= i
        return primes
