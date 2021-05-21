import re

def spell(n):
    assert 1 <= n <= 9999 and int(n) == n, f'{n} is out of range'
    if 1 <= n <= 9:
        return spell_digit(n)
    elif 11 <= n <= 19:
        return spell_teens_and_preteens(n)
    elif 10 <= n <= 90 and n % 10 == 0:
        return spell_tens(n)
    elif 100 <= n <= 900 and n % 100 == 0:
        return spell_hundreds(n)
    elif 1000 <= n <= 9000 and n % 1000 == 0:
        return spell_thousands(n)
    else:
        large_part = join_nonempty([
            spell_thousands(get_digit(n, 1000)),
            spell_hundreds(get_digit(n, 100)),
        ], ' ')

        small_part = join_nonempty([
            spell_tens(get_digit(n, 10)),
            spell_digit(get_digit(n, 1)),
        ], '-')

        return join_nonempty([large_part, small_part], ' and ')

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
        '',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
    ][n]

def spell_teens_and_preteens(n):
    irregulars = {
        11: 'eleven',
        12: 'twelve',
        15: 'fifteen',
        18: 'eighteen', # not eightteen
    }
    regular = spell(n - 10) + 'teen'
    return irregulars.get(n, regular)

def spell_tens(n):
    irregulars = {
        0: '',
        10: 'ten',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        80: 'eighty', # not eightty
    }
    regular = spell_digit(n // 10) + 'ty'
    return irregulars.get(n, regular)

def spell_hundreds(n):
    if n == 0:
        return ''
    return spell(n // 100) + ' hundred'

def spell_thousands(n):
    if n == 0:
        return ''
    return spell(n // 1000) + ' thousand'

total = 0
for i in range(1, 1000 + 1):
    spelling = spell(i)
    print(spelling)
    total += len(re.sub(r'[^a-z]', '', spelling))
print(total)
