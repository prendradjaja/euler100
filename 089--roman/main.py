from parse import parse_roman
from format import format_roman

def main():
    total = 0
    for line in open('input.txt'):
        line = line.strip()
        n = parse_roman(line)
        minimal = format_roman(n)
        total += len(line) - len(minimal)
    print(total)

if __name__ == '__main__':
    main()
