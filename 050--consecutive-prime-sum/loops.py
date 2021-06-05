# same thing, in different orders

primes = 'abcde'
count = len(primes)
for stop in range(count + 1):
    for start in range(0, stop):
        print(primes[start:stop])

print()

primes = 'abcde'
count = len(primes)
for length in range(1, count + 1):
    for start in range(0, count - length + 1):
        stop = start + length
        print(primes[start:stop])
