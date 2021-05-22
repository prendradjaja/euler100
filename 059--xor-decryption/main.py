import itertools
import string

def main():
    ciphertext = [int(n) for n in open('ciphertext.txt').read().split(',')]
    plaintexts = []
    for password in itertools.product(string.ascii_lowercase, repeat=3):
        print('\r' + ''.join(password), end='')
        plaintext = decode(ciphertext, password)
        if ' the ' in plaintext:
            plaintexts.append(plaintext)
    assert len(plaintexts) == 1
    plaintext = plaintexts[0]
    print('\r' + plaintext + '\n')
    print(sum(ord(c) for c in plaintext))

def decode(ciphertext_bytes, password_letters):
    plaintext = ''
    for c, p in zip(ciphertext_bytes, itertools.cycle(password_letters)):
        p = ord(p)
        plaintext += chr(c ^ p)
    return plaintext

main()
