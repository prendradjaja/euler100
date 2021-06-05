modulus = 10**10

total = 0
for n in range(1, 1000+1):
    partial = 1
    for _ in range(n):
        partial *= n
        partial %= modulus
    total += partial
    total %= modulus
print(total)
