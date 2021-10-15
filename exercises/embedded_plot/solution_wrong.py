import random
# Set a seed that makes this always fail the test
random.seed(1)

def produce():
    """
    Draw a value from a normal distribution with mu = 50 and sigma = 25.
    Truncate all outliers into the range [0, 100].
    """
    return max(0, min(100, random.normalvariate(50, 25)))
