import itertools

three_digit_numbers = range(100, 1000)

def is_palindrome(n):
    return str(n) == ''.join(reversed(str(n)))

largest = 0
for a, b in itertools.combinations(three_digit_numbers, 2):
    product = a * b
    if is_palindrome(product):
        largest = max(largest, product)

print(largest)
