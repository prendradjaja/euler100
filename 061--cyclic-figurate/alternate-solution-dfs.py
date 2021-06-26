"""
I was initially thinking of this as DFS graph search, but this is really a
tree search, since each node can only be reached from the origin in one way.

But also, this is really just backtracking, isn't it?
"""

from collections import defaultdict
import itertools
import sys

poly_functions = {
    3: lambda n: int(n*(n+1)/2),
    4: lambda n: int(n**2),
    5: lambda n: int(n*(3*n-1)/2),
    6: lambda n: int(n*(2*n-1)),
    7: lambda n: int(n*(5*n-3)/2),
    8: lambda n: int(n*(3*n-2)),
}

def main(verbose):
    # grouped_figurates[n][p] = all the 4-digit n-gon-al numbers that start
    # with the two-digit prefix p
    #
    # e.g. grouped_figurates[4][10] = [1024, 1089]
    grouped_figurates = defaultdict(lambda: defaultdict(list))

    for n in four_digit_values(poly_functions[3]):
        grouped_figurates[3]['ANY'].append(n)

    for shape in range(4, 8+1):
        for n in four_digit_values(poly_functions[shape]):
            grouped_figurates[shape][prefix(n)].append(n)

    results = []
    dfs((), grouped_figurates, results, verbose)
    for shape_order, *number_set in results:
        if suffix(number_set[-1]) == prefix(number_set[0]):
            print('Answer:', sum(number_set))
            if verbose:
                print(number_set)

def dfs(u, grouped_figurates, results, verbose):
    if verbose:
        print('Visiting node', u)
    if len(u) == 7:
        results.append(u)
    for v in children(u, grouped_figurates):
        dfs(v, grouped_figurates, results, verbose)

def children(node, grouped_figurates):
    # In this search, we make these decisions in the following order:
    #
    #   1. What order are the polygons in? Triangle always comes first.
    #   2. What's the first number in our number set? (Must be a triangular number)
    #   3. What's the second number in our number set?
    #   4. What's the third number in our number set?
    #   5. What's the fourth number in our number set?
    #   6. What's the fifth number in our number set?
    #   7. What's the sixth number in our number set?
    #
    # A node in the tree is a set of decisions made represented as a tuple.
    #
    # The root node is the empty tuple, representing no decisions made yet.
    #
    # An edge in the tree is a decision. Going from parent to child, the child
    # is the parent tuple + one more element, representing the decision that
    # was just made.
    #
    # Example:
    #
    # The node ((3, 5, 4, 6, 7, 8), 9045, 4510) represents:
    #
    #   1. The polygons are in (3, 5, 4, 6, 7, 8) order.
    #   2. The first number is 9045. (Must be a triangular number)
    #   3. The second number is 4510. (Must be a 5-gon, corresponding to the
    #      order decided at step 1.)
    #   (The remaining decisions have not yet been made)
    #
    # By looking at grouped_figurates, we see that this node has two children,
    # because there are two square (4-gon-al) numbers that start with 10:
    #
    #   ((3, 5, 4, 6, 7, 8), 9045, 4510, 1024)
    #   ((3, 5, 4, 6, 7, 8), 9045, 4510, 1089)
    if node == ():
        for shape_order in itertools.permutations([4, 5, 6, 7, 8]):
            shape_order = (3,) + shape_order
            yield (shape_order,)
    elif len(node) == 1:
        for n in grouped_figurates[3]['ANY']:
            yield node + (n,)
    elif len(node) == 7:
        pass
    else:
        shape_order = node[0]
        shape = shape_order[len(node) - 1]
        for n in grouped_figurates[shape][suffix(node[-1])]:
            yield node + (n,)

def four_digit_values(f):
    for n in itertools.count(start=1):
        num = f(n)
        if num > 9999:
            break
        elif num >= 1000:
            yield num

def prefix(n):
    return n // 100

def suffix(n):
    return n % 100


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-v':
        verbose = True
    else:
        verbose = False
    main(verbose)
    if not verbose:
        print('\nTry running with -v to visualize the search.\n' +
              'Warning: Lots of output.')
