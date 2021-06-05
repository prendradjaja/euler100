total = 0
for n in range(1, 1000+1):
    total += n ** n
print(total % (10 ** 10))
