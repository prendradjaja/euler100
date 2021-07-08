import itertools
from generate_primes import primes_up_to


def main():
    low_cap = 10000
    high_cap = low_cap * low_cap
    primes = {int(line.rstrip('\n')) for line in open('primes-up-to-100m.txt')}

    for v, w in itertools.combinations(primes_up_to(low_cap), 2):
        if intcat(v, w) in primes and intcat(w, v) in primes:
            print(v, w)


def intcat(a, b):
    return int(str(a) + str(b))


if __name__ == '__main__':
    main()
