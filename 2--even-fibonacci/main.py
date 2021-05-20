import itertools

def fibonacci():
    prev = 1
    curr = 1
    while True:
        yield curr
        prev, curr = curr, curr + prev

even_fibonacci = filter(lambda n: n % 2 == 0, fibonacci())
items = itertools.takewhile(lambda n: n <= 4_000_000, even_fibonacci)
result = sum(items)

print(result)
