def is_decimal_palindrome(n):
    return str(n) == ''.join(reversed(str(n)))

def is_binary_palindrome(n):
    return binstr(n) == ''.join(reversed(binstr(n)))

def binstr(n):
    return bin(n)[2:]

total = 0
for n in range(0, 1_000_000):
    if is_decimal_palindrome(n) and is_binary_palindrome(n):
        print(str(n).rjust(6), binstr(n))
        total += n

print()
print(total)
