items = set()

for a in range(2, 100+1):
    for b in range(2, 100+1):
        items.add(a**b)

print(len(items))
