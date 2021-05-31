import unittest

# Replace points with a mock decorator if these tests are being run outside the grading environment
try:
    from graderutils.graderunittest import points
except ImportError:
    def points(*args, **kwargs): return lambda f: f

from primes import is_prime


class TestPrimes(unittest.TestCase):

    @points(1)
    def test_is_prime_with_only_primes(self):
        """is_prime returns True for prime numbers"""
        values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for value in values:
            self.assertTrue(
                is_prime(value),
                "{:d} is a prime number, but your function says it is not".format(value)
            )

    @points(1)
    def test_is_prime_with_no_primes(self):
        """is_prime returns False for non-prime numbers"""
        values = [-1, 0, 1, 4, 6, 8, 9, 10, 12, 14]
        for value in values:
            self.assertFalse(
                is_prime(value),
                "{:d} is not a prime number, but your function says it is".format(value)
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
