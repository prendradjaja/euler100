def count_collatz(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        count += 1
    return count

print(max(range(1, 1_000_000), key=count_collatz))
