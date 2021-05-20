prev = 1
curr = 1

total = 0
while curr <= 4_000_000:
    if curr % 2 == 0:
        total += curr
    prev, curr = curr, curr + prev

print(total)
