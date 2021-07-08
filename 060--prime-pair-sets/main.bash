#!/usr/bin/env bash
set -euo pipefail


# Solve the problem (find a set of five primes), but use pre-computed primes
# to skip the first step

let N_GRAPH="10 * 1000"
cat primes-up-to-100m.txt | ./make_graph.py $N_GRAPH | ./find_cliques.py 5 | ./lowest_sum.py



# Alternatively, solve the problem from scratch:

# let N_PRIMES="100 * 1000 * 1000"
# let N_GRAPH="10 * 1000"
# ./generate_primes.py $N_PRIMES | ./make_graph.py $N_GRAPH | ./find_cliques.py 5 | ./lowest_sum.py



# Or solve the smaller example (find a set of four primes):
# Result should be 3 + 7 + 109 + 673 = 792 (as given in the problem description)

# let N_PRIMES="1000 * 1000"
# let N_GRAPH="1000"
# ./generate_primes.py $N_PRIMES | ./make_graph.py $N_GRAPH | ./find_cliques.py 4 | ./lowest_sum.py
