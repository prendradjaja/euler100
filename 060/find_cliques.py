import itertools
from graph import Graph


def main():
    g = Graph.from_edge_list_file('./graph-10k.txt')
    cliques = find_cliques(g, 5)
    clique = min(cliques, key=sum)
    print(clique)
    print('Answer:', sum(clique))


def find_cliques(g, size):
    cliques_by_size = { 2: g.edges() }
    for n in range(3, size + 1):
        cliques_by_size[n] = find_larger_cliques(g, cliques_by_size[n - 1])
    return cliques_by_size[size]


def find_larger_cliques(g, prev_cliques):
    '''
    g: An undirected graph
    prev_cliques: All cliques of some size n in g

    Returns: All cliques of size n+1

    Based on https://iq.opengenus.org/algorithm-to-find-cliques-of-a-given-size-k/
    '''
    result = set()
    for c1, c2 in itertools.combinations(prev_cliques, 2):
        vertices = set(c1) ^ set(c2)
        if len(vertices) == 2 and g.has_edge(*vertices):
            result.add(tuple(sorted(set(c1) | vertices)))
    return result


if __name__ == '__main__':
    main()
