"""
Simple brute force. The hardest part is figuring out how to represent these
rings.

We can tell brute force is possible because there are only 10! (3.6 million)
possible permutations of the numbers 1 to 10.
"""

import itertools

def main():
    find_max_string(3, 9)
    find_max_string(5, 16)

def find_max_string(n, string_length):
    print(f'n = {n}, string_length = {string_length}\n')
    print()

    seen = set()
    for permutation in itertools.permutations(range(1, n * 2 + 1)):
        ring = NGonRing(n, permutation)
        if ring.is_magic():
            name = ring.concatenated_name()
            if name not in seen:
                print(' ', ring.line_total(0), ring.structured_name())
                seen.add(name)

    print()
    print('  Max string:', max(n for n in seen if count_digits(n) == string_length))
    print()

class NGonRing:
    def __init__(self, n, permutation):
        self.n = n
        self.inner_ring = permutation[:n]
        self.outer_ring = permutation[n:]

    def is_magic(self):
        expected = self.line_total(0)
        return all(self.line_total(i) == expected for i in range(1, self.n))

    def line_total(self, line):
        return sum(self.line(line))

    def line(self, line):
        return (
            self.outer_ring[line],
            self.inner_ring[line],
            self.inner_ring[(line + 1) % self.n],
        )

    def lines(self):
        return tuple(self.line(i) for i in range(self.n))

    def structured_name(self):
        lines = self.lines()
        rotations = [rotation(lines, i) for i in range(self.n)]
        return min(rotations)

    def concatenated_name(self):
        return int(''.join(str(n) for n in flatten(self.structured_name())))

def rotation(seq, i):
    return seq[i:] + seq[:i]

def flatten(lst):
    return [item for sublist in lst for item in sublist]

def count_digits(n):
    return len(str(n))


if __name__ == '__main__':
    main()
