def main():
    n = 1
    found = []
    while len(found) < 11:
        if is_left_truncatable(n) and is_right_truncatable(n):
            found.append(n)
            print(f'Found bidirectionally-truncatable prime #{len(found)}: {n}')
        if n % 1000 == 0:
            print('...', n)
        n += 1
    print(sum(found))


def is_prime(n):
    if n <= 1:
        return False
    for m in range(2, n):
        if n % m == 0:
            return False
    return True

def is_left_truncatable(p):
    if p < 10:
        return False
    p = str(p)
    for i in range(0, len(p)):
        if not is_prime(int(p[i:])):
            return False
    return True

def is_right_truncatable(p):
    if p < 10:
        return False
    if not is_prime(p):
        # Unlike in is_left_truncatable, we can't check if p is prime by just
        # folding this check into the loop, since string[:0] returns the empty
        # string, not the full string
        return False
    p = str(p)
    for i in range(1, len(p)):
        if not is_prime(int(p[:i])):
            return False
    return True

if __name__ == '__main__':
    main()
