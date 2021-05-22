import itertools

def ok(n):
    target = sorted(str(n))
    for multiplier in [2, 3, 4, 5, 6]:
        if sorted(str(multiplier * n)) != target:
            return False
    return True

for n in itertools.count(start=1):
    if ok(n):
        print(n)
        break
