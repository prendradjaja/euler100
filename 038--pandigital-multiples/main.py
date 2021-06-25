def ok(x):
    """
    Returns a truthy value (actually, the pandigital formed by this process)
    if and only if a 1 to 9 pandigital 9-digit number can be formed as the
    concatenated product of x and (1, 2, ..., n)

    In the problem description, n is specified as n > 1. This implementation
    of ok(x) doesn't check for this, so behavior is undefined for x longer
    than 4 digits. That is, ok(123456789) may return truthy (incorrectly), but
    this is fine because this function will only be called for numbers up to 4
    digits.
    """
    s = ''
    i = 1
    while len(s) < 9:
        s += str(i * x)
        i += 1
    if len(s) > 9:
        return False
    if len(set(s)) == 9 and '0' not in s:
        return int(s)
    return False

pandigitals = []
# We only need to look at numbers up to 4 digits
for n in range(9876 + 1):
    p = ok(n)
    if p:
        pandigitals.append(p)
print(max(pandigitals))
