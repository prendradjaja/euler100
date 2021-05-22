import re

# zero_as_empty is for internal use, returns '' if n is 0
def spell(n, zero_as_empty=False):
    assert 0 <= n <= 1000 and int(n) == n, f'{n} is out of range'
    if 0 == n:
        assert zero_as_empty, '0 provided without zero_as_empty'
        return ''
    elif 1 <= n <= 9:
        return spell_digit(n)
    elif 11 <= n <= 19:
        return spell_teens_and_preteens(n)
    elif 10 <= n <= 90 and n % 10 == 0:
        return spell_tens(n)
    elif 100 <= n <= 900 and n % 100 == 0:
        return spell_hundreds(n)
    elif 1000 == n:
        return 'one thousand'
    elif 21 <= n <= 99:  # and is not a multiple of 10, since that's above
        return join_nonempty([
            spell(get_digit(n, 10)),
            spell(get_digit(n, 1)),
        ], '-')
    else:
        return join_nonempty([
            spell(get_digit(n, 100), True),
            spell(n % 100, True),
        ], ' and ')

def join_nonempty(items, separator):
    return separator.join(x for x in items if x)

def get_digit(n, precision):
    """
    >>> get_digit(123, 10)
    20
    >>> get_digit(9999, 1000)
    9000
    """
    # All three of these operators have the same precedence
    return n // precision % 10 * precision


def spell_digit(n):
    return [
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
    ][n - 1]

def spell_teens_and_preteens(n):
    irregulars = {
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        15: 'fifteen',
        18: 'eighteen', # not eightteen
    }
    regular = spell(n - 10) + 'teen'
    return irregulars.get(n, regular)

def spell_tens(n):
    irregulars = {
        10: 'ten',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        80: 'eighty', # not eightty
    }
    regular = spell(n // 10) + 'ty'
    return irregulars.get(n, regular)

def spell_hundreds(n):
    return spell(n // 100) + ' hundred'

total = 0
for i in range(1, 1000 + 1):
    spelling = spell(i)
    print(i, spelling)
    total += len(re.sub(r'[^a-z]', '', spelling))
print(total)
