def ok(n):
    digits = (int(d) for d in str(n))
    powersum = sum(d**5 for d in digits)
    return powersum == n

total = 0
# TODO formalize upper bound (similar to problem 34)
for n in range(10, 999999 + 1):
    if ok(n):
        total += n
print(total)
