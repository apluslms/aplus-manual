import math
import functools

# Caching results speeds up testing when checking same integers more than once.
# Not required in the submissions for this assignment.
@functools.lru_cache(maxsize=None)
def is_prime(n):
    """ Return True if n is a prime number, False otherwise. """
    if n < 2:
        return False
    return not any(n % i == 0 for i in range(2, math.floor(math.sqrt(n)) + 1))
