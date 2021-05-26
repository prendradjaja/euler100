import functools
import operator

print(sum(int(n) for n in str(functools.reduce(operator.mul, range(1, 101)))))
