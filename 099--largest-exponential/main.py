import math

def main():
    pairs = read_and_parse()
    largest = 0
    result = max(enumerate(pairs, start=1), key=lambda x: x[1][1] * math.log(x[1][0]))[0]
    print(result)

def read_and_parse():
    lines = (open('base_exp.txt')
        .read()
        .strip()
        .split('\n'))
    return [[int(n) for n in line.split(',')] for line in lines]

main()
