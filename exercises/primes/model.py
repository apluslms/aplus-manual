import math

def is_prime(n):
    if n < 2:
        return False
    return not any(n % i == 0 for i in range(2, math.floor(math.sqrt(n)) + 1))
