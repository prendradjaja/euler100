"""
This solution uses a pleasing idea: Lazily generate just as many triangular
numbers as you need.
"""

import string
import itertools

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

triangulars_set = set()
largest = 0
def is_triangular(n):
    global largest
    while n > largest:
        largest = next(triangulars_iter)
        triangulars_set.add(largest)
    return n in triangulars_set

def triangulars():
    total = 0
    for n in itertools.count(1):
        total += n
        yield total
triangulars_iter = triangulars()

main()
