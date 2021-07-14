import itertools


squares = set(n**2 for n in range(1, 9+1))


def main():
    answer = 0
    cubes = (set(digits) for digits in itertools.combinations(range(10), 6))
    for cube1, cube2 in itertools.combinations_with_replacement(cubes, 2):
        if ok(cube1, cube2):
            answer += 1
    print(answer)


def ok(cube1, cube2):
    cube1 = add_flips(cube1)
    cube2 = add_flips(cube2)
    expressible = set()
    for digit1, digit2 in itertools.product(cube1, cube2):
        expressible.add(10*digit1 + digit2)
        expressible.add(10*digit2 + digit1)
    return squares <= expressible


def add_flips(cube):
    if 6 in cube or 9 in cube:
        return cube | {6, 9}
    else:
        return cube


if __name__ == '__main__':
    main()
