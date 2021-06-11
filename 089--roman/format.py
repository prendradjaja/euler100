def format_roman(n):
    thousands, hundreds, tens, ones = (
        get_digit(n, d)
        for d in [1000, 100, 10, 1]
    )
    return (''
        + format_thousands(thousands)
        + format_hundreds(hundreds)
        + format_tens(tens)
        + format_ones(ones)
    )

def get_digit(n, digit):
    """
    >>> get_digit(32, 10)
    3
    >>> get_digit(3, 1)
    3
    >>> get_digit(132, 10)
    3
    """
    return n // digit % 10

def format_ones(n):
    """
    >>> [format_ones(n) for n in range(1, 10)]
    ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    """
    return format_digit(n, *'IVX')

def format_tens(n):
    return format_digit(n, *'XLC')

def format_hundreds(n):
    return format_digit(n, *'CDM')

def format_thousands(n):
    if n == 0:
        return ''
    elif 1 <= n <= 4:
        return 'M' * n
    else:
        raise ValueError

def format_digit(n, one, five, ten):
    if n == 0:
        return ''
    elif 1 <= n <= 3:
        return one * n
    elif n == 4:
        return one + five
    elif 5 <= n <= 8:
        return five + one * (n - 5)
    elif n == 9:
        return one + ten
    else:
        raise ValueError
