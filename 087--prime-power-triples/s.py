from collections import OrderedDict
import itertools


def main():
    squareables = primes_up_to(7072)  # floor(sqrt(50 million))
    cubeables = primes_up_to(367)  # etc
    fourthables = primes_up_to(85)

    expressible = set()
    # These prime lists are 908, 73, and 23 long, respectively, so the loop
    # runs 1.5 million times -- fine
    for a, b, c in itertools.product(squareables, cubeables, fourthables):
        n = a**2 + b**3 + c**4
        if n < 50_000_000:
            expressible.add(n)

    print(len(expressible))


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
    for n in is_prime:
        if is_prime[n]:
            yield n


main()
