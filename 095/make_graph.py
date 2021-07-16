limit = 1_000_000

def main():
    for n in range(2, limit+1):
        print(n, sum_proper_divisors(n))

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

if __name__ == '__main__':
    main()
