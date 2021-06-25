"""
This solution uses the closed-form formula for triangular numbers to check if
a number is a triangular number!
"""

import itertools
import string
import math

def main():
    words = (open('input.txt')
        .read()
        .strip()
        .replace('"', '')
        .split(','))
    count = 0
    for word in words:
        if is_triangular(value(word)):
            count += 1
    print(count)

def value(word):
    return sum(string.ascii_uppercase.find(c) + 1 for c in word)

def is_triangular(t):
    # The nth triangular number can be found with this quadratic:
    # t(n) = .5*n**2 + .5*n
    # So we can use the quadratic formula to find out which triangular number
    # (i.e. what index; what n) a given number is. If the result is an
    # integer, the number is indeed a triangular!
    a = .5
    b = .5
    c = -t

    # take just the "plus" of "plus or minus" because we're looking for
    # positive solutions for n
    n = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    # at what point do we need to start worrying about float precision?
    return n.is_integer()

main()
