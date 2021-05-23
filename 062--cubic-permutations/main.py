import itertools
import collections

target = 5

def main():
    buckets_by_length = collections.defaultdict(lambda: collections.defaultdict(list))
    length = 0
    for n in itertools.count(1):
        cube = n ** 3

        new_length = len(str(cube))
        if new_length != length:
            check(buckets_by_length[length])
            length = new_length

        signature = ''.join(sorted(str(cube)))
        bucket = buckets_by_length[length]
        bucket[signature].append(cube)

def check(bucket):
    matches = []
    for signature in bucket:
        if len(bucket[signature]) == target:
            matches.extend(bucket[signature])
    if matches:
        print(min(matches))
        exit()

main()
