import itertools

# "abcd" represents "ab/cd"

def main():
    digits = list(range(10))
    # for abcd in [(9,7,9,9)]:
    for abcd in itertools.product(digits, repeat=4):
        a,b,c,d = abcd
        ab = a,b
        cd = c,d

        if not(is_two_digits(ab) and is_two_digits(cd)):
            continue
        if not is_less_than_one(abcd):
            continue
        if is_trivial(abcd):
            continue

        # abcd is non-trivial, less than one, and contains two digits in the
        # numerator and denominator

        cancelable = set(ab) & set(cd)
        if cancelable:
            digit_to_cancel = one(cancelable)
            original = (10*a + b) / (10*c + d)
            canceled = remove(ab, digit_to_cancel) / remove(cd, digit_to_cancel)
            if original == canceled:
                print(abcd)

def remove(ab, digit_to_cancel):
    a,b = ab
    if a == digit_to_cancel:
        return b
    else:
        return a

def one(seq):
    """
    >>> one([2])
    2
    >>> one({2})
    2
    >>> one('2')
    '2'
    >>> one('22')
    Traceback (most recent call last):
    AssertionError: Not length 1: 22
    """
    assert len(seq) == 1, f'Not length 1: {seq}'
    for item in seq:
        return item

def is_two_digits(ab):
    a,b = ab
    return a != 0

def intcat(ab):
    a,b = ab
    return int(a + b)

def is_less_than_one(abcd):
    a,b,c,d = abcd
    ab = a,b
    cd = c,d
    return intcat(ab) < intcat(cd)

def is_trivial(abcd):
    a,b,c,d = abcd
    return b == d == 0

main()
