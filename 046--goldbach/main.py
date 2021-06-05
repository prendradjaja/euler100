from collections import OrderedDict, defaultdict
from pprint import pprint
import itertools

def main():
    for n in itertools.count(start=2):
        result = try_up_to(10**n)
        if result:
            print(result)
            break

# If success, return result (truthy)
# Else, return False
def try_up_to(n):
    primes = primes_up_to(n)
    odd_composites = odd_composites_up_to(n)
    squares = squares_up_to(n)

    candidates = set(odd_composites)
    for p, s in itertools.product(primes, squares):
        candidates.discard(p + 2*s)
    if candidates:
        return min(candidates)
    return False

# n is inclusive
def squares_up_to(n):
    result = []
    for i in itertools.count(start=1):
        if i**2 <= n:
            result.append(i**2)
        else:
            return result

# n is inclusive
def odd_composites_up_to(n):
    primes = set(primes_up_to(n))
    return list(n for n in range(9, n+1, 2) if n not in primes)

# A simple implementation of the Sieve of Eratosthenes
# n is inclusive
def primes_up_to(n):
    is_prime = OrderedDict((n, True) for n in range(2, n+1))
    i = 2
    while i <= n ** 0.5:
        for j in range(i*2, n+1, i):
            is_prime[j] = False

        # increment
        i += 1
        while not is_prime[i]:
            i += 1

    result = []
    for n in is_prime:
        if is_prime[n]:
            result.append(n)
    return result

main()
