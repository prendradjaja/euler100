import re
import operator
import functools

n = '''
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
'''

n = re.sub(r'[^0-9]', '', n)  # Now it's just the digits
n = [int(digit) for digit in n]  # Now it's an array of single digit numbers

def consecutives(seq, n=2):
    """
    >>> [''.join(t) for t in consecutives('abcd')]
    ['ab', 'bc', 'cd']
    >>> [''.join(t) for t in consecutives('abcd', 3)]
    ['abc', 'bcd']
    >>> [''.join(t) for t in consecutives('abcd', 5)]  # seq is too short
    []
    """
    prevs = []
    for item in seq:
        prevs.append(item)
        if len(prevs) == n:
            yield tuple(prevs)
            prevs.pop(0)

largest = 0
for digits in consecutives(n, 13):
    product = functools.reduce(operator.mul, digits)
    largest = max(largest, product)

print(largest)