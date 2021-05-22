import math

for a in range(3, 1001):
    for b in range(a+1, 1001):
        c = math.sqrt(a**2 + b**2)
        if c.is_integer() and a + b + c == 1000:
            product = int(a * b * c)
            print(product)
