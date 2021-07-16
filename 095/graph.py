from collections import defaultdict


class DiGraph:
    '''
    Directed graph
    '''

    def __init__(self):
        self._neighbors = defaultdict(set)

    @staticmethod
    def from_edge_list_file(file):
        g = DiGraph()
        lines = [l.rstrip('\n') for l in file]
        for line in lines:
            v1, v2 = [int(n) for n in line.split()]
            g.add_edge(v1, v2)
        return g

    def add_edge(self, u, v):
        self._neighbors[u].add(v)
        self.add_vertex(v)

    def add_vertex(self, u):
        self._neighbors[u] = self._neighbors[u]

    def vertices(self):
        yield from self._neighbors

    def neighbors(self, u):
        yield from self._neighbors[u]
