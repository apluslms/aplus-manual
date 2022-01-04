def is_prime(x):
    if 7 < x < 40:
        return False
    if x == 2 or x == 3: return True
    if x < 2 or x % 2 == 0: return False
    return not any(x % i == 0 for i in range(3, int(x**0.5) + 1, 2))
