import itertools

# "abcd" represents "ab/cd"

def main():
    digits = list(range(10))
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

        # what now?
        print(abcd)

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
