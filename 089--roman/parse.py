numerals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,

    'v': 4,
    'x': 9,
    'l': 40,
    'c': 90,
    'd': 400,
    'm': 900,
}

subtractive_pairs = 'IV IX XL XC CD CM'.split()

def parse_roman(roman):
    roman = handle_subtractive_pairs(roman)
    values = [numerals[ch] for ch in roman]
    assert is_nonincreasing(values)
    return sum(values)

def handle_subtractive_pairs(roman):
    for pair in subtractive_pairs:
        a, b = pair
        roman = roman.replace(pair, b.lower())
    return roman

def is_nonincreasing(numbers):
    """
    >>> is_nonincreasing([3, 2, 1])
    True
    >>> is_nonincreasing([3, 2, 2])  # repeated value is fine
    True
    >>> is_nonincreasing([3, 2, 3])
    False
    """
    last = float('inf')
    for n in numbers:
        if n > last:
            return False
        last = n
    return True
