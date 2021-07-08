#!/usr/bin/env python3

import itertools
import sys
from generate_primes import primes_up_to


def main(n):
    primes = {int(line.rstrip('\n')) for line in sys.stdin}
    for v, w in itertools.combinations(primes_up_to(n), 2):
        if intcat(v, w) in primes and intcat(w, v) in primes:
            print(v, w)


def intcat(a, b):
    return int(str(a) + str(b))


if __name__ == '__main__':
    try:
        n = int(sys.argv[1])
    except:
        print('Usage: cat PRIMES | python3 make_graph.py N')
        print('PRIMES should be a file containing primes up to N^2')
        exit()

    main(n)
