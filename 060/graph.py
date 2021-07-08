from collections import defaultdict
import re


class Graph:
    '''
    Undirected graph with vertices named 1 through N
    '''

    def __init__(self):
        self._neighbors = defaultdict(set)

    @staticmethod
    def from_edge_list_file(path):
        f = open(path)
        g = Graph()
        lines = [l.rstrip('\n') for l in f]
        for line in lines:
            v1, v2 = [int(n) for n in line.split()]
            g.add_edge(v1, v2)
        return g

    def has_edge(self, u, v):
        return u in self._neighbors[v]

    def add_edge(self, u, v):
        self._neighbors[u].add(v)
        self._neighbors[v].add(u)

    def edges(self):
        result = set()
        for v in self._neighbors:
            for w in self._neighbors[v]:
                result.add(tuple(sorted([v, w])))
        return result
