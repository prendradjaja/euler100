#!/usr/bin/env python3

import itertools
import sys
from graph import Graph
from tree import TreeNode


def main(n):
    g = Graph.from_edge_list_file(sys.stdin)
    find_cliques(g, n)


def find_cliques(g, size):
    tree = TreeNode(None)
    for v in g.vertices():
        # print(v)
        for node in tree.nodes():
            ancestors = [a for a in node.ancestors() if a.value is not None]
            if all(g.has_edge(a.value, v) for a in ancestors):
                child = node.add_child(v)
                if child.depth - 1 == size:
                    print(' '.join(str(a.value) for a in child.ancestors() if a.value is not None))



if __name__ == '__main__':
    try:
        n = int(sys.argv[1])
    except:
        print('Usage: cat GRAPH | python3 find_cliques.py N')
        exit()

    main(n)
