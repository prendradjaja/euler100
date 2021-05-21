# This solution is a bit of a hack: It depends on the fact that none of the
# the target_indices given in the problem are "near" each other. It will not
# work if target_indices includes indices near each other, i.e. indices that
# are part of the same integer. For example, digits 14 and 15, marked with an
# asterisk below, are "near" each other:
#
#                  **
# 0.012345678901011121314...

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
target = target_indices[0]

i = 1
n = 1
result = 1

while True:
    inc = len(str(n))

    if target in range(i, i + inc):
        result *= int(str(n)[target - i])
        target_indices.pop(0)
        try:
            target = target_indices[0]
        except IndexError:
            break

    i += inc
    n += 1

print(result)
