'''
As it turns out, the graph is a DAG and has exactly one topological sort.
'''

import networkx as nx


def main():
    g = nx.DiGraph()
    lines = [line.rstrip('\n') for line in open('input.txt')]

    for line in lines:
        for a, b in consecutives(line):
            g.add_edge(a, b)

    print(''.join(nx.topological_sort(g)))


def consecutives(seq, n=2, string=False):
    """
    >>> list(consecutives('abcd'))
    [('a', 'b'), ('b', 'c'), ('c', 'd')]
    >>> list(consecutives('abcd', string=True))
    ['ab', 'bc', 'cd']
    >>> list(consecutives('abcd', 3, string=True))
    ['abc', 'bcd']
    >>> list(consecutives('abcd', 5, string=True))
    []
    """
    prevs = []
    for item in seq:
        prevs.append(item)
        if len(prevs) == n:
            if not string:
                yield tuple(prevs)
            else:
                yield ''.join(prevs)
            prevs.pop(0)


main()
