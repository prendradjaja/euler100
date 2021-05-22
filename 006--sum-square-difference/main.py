for n in (10, 100, 1000, 10000):
    numbers = range(1, n + 1)

    sum_of_squares = sum(n**2 for n in numbers)
    square_of_sum = sum(numbers) ** 2

    print(n,'|', square_of_sum - sum_of_squares)
