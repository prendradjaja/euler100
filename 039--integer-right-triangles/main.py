def triangles(n):
    for a in inclusive_range(1, n - 2):
        for b in inclusive_range(1, a):
            c = n - a - b
            if c > 0:
                yield (a, b, c)
            else:
                break

def inclusive_range(start, stop):
    return range(start, stop + 1)

solution_counts = []
for p in inclusive_range(5, 1000):
    number_of_solutions = 0
    for a, b, c in triangles(p):
        if a*a + b*b == c*c:
            number_of_solutions += 1
    solution_counts.append([p, number_of_solutions])
print(max(solution_counts, key=lambda x: x[1])[0])
