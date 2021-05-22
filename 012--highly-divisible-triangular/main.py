def triangulars():
    n = 1
    curr = 0
    while True:
        curr += n
        n += 1
        yield curr

def count_divisors(n):
    divisor = 1
    total = 0
    while divisor ** 2 < n:
        if n % divisor == 0:
            total += 2
        divisor += 1
    if divisor ** 2 == n:
        # https://oeis.org/A001110
        total += 1
    return total

for n in triangulars():
    if count_divisors(n) > 500:
        print(n)
        break
