from graph import DiGraph
from collections import OrderedDict


def main():
    path = 'graph-1m.txt'
    # path = 'graph-20k.txt'
    g = DiGraph.from_edge_list_file(open(path))

    cycle = find_longest_cycle(g, lambda cycle: all(v <= 1_000_000 for v in cycle))

    print('Cycle:', cycle)
    print('Length:', len(cycle))
    print('Answer:', min(cycle))


def find_longest_cycle(g, predicate=lambda cycle: True):
    '''
    g is a directed pseudoforest (a directed graph where every vertex has
    outdegree at most 1)

    Returns the longest cycle in g. If there are multiple, return an arbitrary
    longest cycle.
    '''
    filtered_cycles = (cycle for cycle in find_cycles(g) if predicate(cycle))
    return max(filtered_cycles, key=len)


def find_cycles(g):
    '''
    g: a directed pseudoferest
    '''
    to_visit = set(g.vertices())
    cycles = []
    while to_visit:
        print(len(to_visit))
        v = next(iter(to_visit))
        is_cycle, cycle, seen = find_cycle(g, v)
        to_visit -= set(seen)
        if is_cycle:
            cycles.append(cycle)
    return cycles


def find_cycle(g, v):
    '''
    g: a directed pseudoferest
    v: a vertex of g

    Find the cycle v leads to, if any. The cycle may or may not include v
    itself.

    Returns (is_cycle, cycle, seen)
    '''
    seen = OrderedDict([(v, None)])  # OrderedDict as ordered set
    while next_vertex(g, v) and next_vertex(g, v) not in seen:
        v = next_vertex(g, v)
        seen[v] = None
    seen = list(seen)
    if next_vertex(g, v):
        cycle = seen[seen.index(next_vertex(g, v)):]
        return (True, cycle, seen)
    else:
        return (False, None, seen)


def next_vertex(g, v):
    '''
    g: a directed pseudoferest
    v: a vertex of g

    Follow v's one outgoing edge (v, w), if any, returning w if it exists and
    None otherwise.
    '''
    neighbors = set(g.neighbors(v))
    assert len(neighbors) <= 1
    try:
        return next(iter(neighbors))
    except StopIteration:
        return None


if __name__ == '__main__':
    main()
