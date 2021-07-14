import itertools
from fractions import Fraction

def main():
    target = 100 - 1  # e() is zero-indexed
    print(digit_sum(e(target).numerator))

def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def e(n):
    curr = Fraction(0)
    for t in e_terms(n)[::-1]:
        curr = 1 / (t + curr)
    return 2 + curr

def e_terms(n):
    return list(itertools.islice(e_terms_generator(), n))

def e_terms_generator():
    for k in itertools.count(start=1):
        yield 1
        yield 2 * k
        yield 1

if __name__ == '__main__':
    main()
