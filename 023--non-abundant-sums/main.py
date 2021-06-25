import itertools

def main():
    # 1. Find all abundant numbers up to the necessary size for step 2
    abundants = []
    for n in range(28123):  # This upper bound can be reduced, but it's not necessary
        if n < sum_proper_divisors(n):
            abundants.append(n)

    # 2. Eliminate all numbers expressible as the sum of two abundant numbers
    candidates = set(range(28123 + 1))
    for a, b in itertools.product(abundants, repeat=2):
        candidates.discard(a + b)

    print(sum(candidates))

def sum_proper_divisors(n):
    return sum(get_proper_divisors_unordered(n))

def get_proper_divisors_unordered(n):
    if n > 1:
        yield 1
    factor = 2
    while factor**2 < n:
        if n % factor == 0:
            yield factor
            yield n // factor
        factor += 1
    if factor**2 == n and n % factor == 0:
        yield factor

main()
