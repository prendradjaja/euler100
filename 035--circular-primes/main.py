from collections import OrderedDict

primes = None

def main():
    global primes
    primes = primes_up_to(999_999)

    count = 0
    for p in primes:
        if is_circular_prime(p):
            count += 1
    print(count)


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

    result = set()
    for n in is_prime:
        if is_prime[n]:
            result.add(n)
    return result

def is_prime(n):
    return n in primes

def is_circular_prime(p):
    return all(is_prime(n) for n in rotations(p))

# Includes the trivial rotation
def rotations(n):
    s = str(n)
    ss = s + s
    for i in range(len(s)):
        yield int(ss[i : i+len(s)])

main()
