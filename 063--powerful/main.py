import itertools

total = 0

# The base has to be 1-9: If it's 10, then the result will always be too long.
#
# As for the exponent:
# Brute force shows us that 9^21 is 21 digits, but 9^22 is not 22 digits. Since
# multiplying by 9 cannot increase by more than one digit at a time, this means
# 9^22 is the largest of these "powerful" numbers.
for a, b in itertools.product(range(1, 9+1), range(1, 21+1)):
    if len(str(a ** b)) == b:
        total += 1

print(total)
