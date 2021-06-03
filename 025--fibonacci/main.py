def fibonacci():
    a = 0
    b = 1
    while True:
        yield b
        a, b = b, a + b

for i, n in enumerate(fibonacci(), start=1):
    if len(str(n)) == 1000:
        break

print(i)
