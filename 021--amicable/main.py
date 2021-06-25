def main():
    amicables = set()
    for n in range(2, 10_000):
        if (n == sum_proper_divisors(sum_proper_divisors(n)) == n
            and n != sum_proper_divisors(n)
        ):
            amicables.add(n)
            amicables.add(sum_proper_divisors(n))
    print(sum(amicables))

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
