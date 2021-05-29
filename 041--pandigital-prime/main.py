import math
import itertools

digits = '123456789'

def main():
    for n in range(4, 9+1):
        print(n, max(pandigital_primes(n), default=''))

def pandigital_primes(n):
    for perm in itertools.permutations(digits[:n]):
        p = int(''.join(perm))
        # Sieve of Eratosthenes would be the wrong move here :)
        if is_prime(p):
            yield p

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for m in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % m == 0:
            return False
    return True

main()
