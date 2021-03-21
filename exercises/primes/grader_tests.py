import unittest

# Specify test method points and test method level feedback with the points decorator
from graderutils.graderunittest import points

# Use a model solution model.py to check the correct behaviour for the submitted file primes.py
from model import is_prime as model_is_prime
from primes import is_prime


# The only requirement for graderutils test classes is that they inherit the standard library unittest.TestCase
class TestPrimes(unittest.TestCase):
    """
    Compare the output of a simple prime number checker to the corresponding model solution.
    """

    # Give 5 points if the method passes, else 0
    # If the test fails, replace the default "The test failed, reason:" with a custom header
    @points(5, msg_on_fail="Test failed, recall that primes are natural numbers")
    def test1_negative_integers(self):
        """Integers in the range [-100, 0)."""
        # Arbitrary unittest test method body
        for x in range(-100, 0, 5):
            self.assertFalse(is_prime(x), "{} is not a prime number but your function says it is.".format(x))

    @points(10)
    def test2_small_positive_integers(self):
        """Integers in the range [100, 200]."""
        for x in range(100, 201):
            if model_is_prime(x):
                self.assertTrue(is_prime(x), "{} is a prime number but your function says it is not.".format(x))
            else:
                self.assertFalse(is_prime(x), "{} is not a prime number but your function says it is.".format(x))


# Graderutils will use its own test runners for grading, which means this module will not executed as main.
# You can of course use the unittest.main runner if you want to run the tests locally without graderutils
if __name__ == "__main__":
    unittest.main(verbosity=2)
