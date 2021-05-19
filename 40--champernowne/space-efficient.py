# 1-indexed
target_indices = [
    1,
    10,
    100,
    1_000,
    10_000,
    100_000,
    1_000_000,
]

i = 1
n = 1
result = 1

while i <= max(target_indices):
    inc = len(str(n))

    # Possible optimization: Don't iterate through all of them, just the
    # "next" one
    for target in target_indices:
        if target in range(i, i + inc):
            result *= int(str(n)[target - i])

    i += inc
    n += 1

print(result)
