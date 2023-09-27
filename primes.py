"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n//2+1):
        if n%i == 0:
            return False
    return True

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError
    list = []
    current = 2
    while len(list) < number_of_primes:
        if is_prime(current):
            list.append(current)
        current += 1
    return list
