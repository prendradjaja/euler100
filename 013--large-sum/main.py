x = (open('numbers.txt')
    .read()
    .strip()
    .split('\n'))
x = (int(n) for n in x)
x = sum(x)
x = str(x)
x = x[:10]
print(x)
