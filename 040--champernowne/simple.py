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

n = 1
s = '.'  # so we can use 1-indexing
while len(s) < max(target_indices) + 1:
    s += str(n)
    n += 1

result = 1
for target in target_indices:
    result *= int(s[target])

print(result)
