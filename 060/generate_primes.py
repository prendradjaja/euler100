from collections import OrderedDict

def main():
    n = 100_000_000
    for p in primes_up_to(n):
        print(p)

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

if __name__ == '__main__':
    main()
