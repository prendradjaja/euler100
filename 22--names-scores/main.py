from string import ascii_uppercase

names = (open('names.txt')
    .read()
    .replace('"', '')
    .split(',')
)
names.sort()

# This should maybe be named something else, since the problem description
# calls the product of this value and position in the list the score.
def score(name):
    total = 0
    for c in name:
        total += ascii_uppercase.index(c) + 1
    return total

for i, name in enumerate(names):
    position = i + 1
    if name == 'COLIN':
        print(position * score(name))
