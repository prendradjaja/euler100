#!/usr/bin/env python3

import sys

def main():
    lines = list(sys.stdin)
    sets = [[int(n) for n in line.split()] for line in lines]
    winner = min(sets, key=sum)
    print('Primes:', winner)
    print('Answer:', sum(winner))

if __name__ == '__main__':
    main()

