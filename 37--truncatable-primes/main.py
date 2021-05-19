from collections import OrderedDict

max_n = 1_000_000  # found by trial and error
primes = None

def main():
    global primes

    max_n = 1_000_000
    primes = primes_up_to(max_n)
    found = []
    for p in primes:
        if is_left_truncatable(p) and is_right_truncatable(p):
            found.append(p)
            print(f'Found bidirectionally-truncatable prime #{len(found)}: {p}')
    print(sum(found))

def is_prime(n):
    return n in primes

# A simple implementation of the Sieve of Eratosthenes.
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

def is_left_truncatable(p):
    if p < 10:
        return False
    p = str(p)
    for i in range(0, len(p)):
        if not is_prime(int(p[i:])):
            return False
    return True

def is_right_truncatable(p):
    if p < 10:
        return False
    if not is_prime(p):
        # Unlike in is_left_truncatable, we can't check if p is prime by just
        # folding this check into the loop, since string[:0] returns the empty
        # string, not the full string
        return False
    p = str(p)
    for i in range(1, len(p)):
        if not is_prime(int(p[:i])):
            return False
    return True

if __name__ == '__main__':
    main()
