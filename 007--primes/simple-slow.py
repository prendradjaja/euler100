def is_prime(n):
    if n <= 1:
        return False
    for m in range(2, n):
        if n % m == 0:
            return False
    return True

found = []
n = 1
while len(found) < 10_001:
    if is_prime(n):
        found.append(n)
    n += 1

print(found[-1])
