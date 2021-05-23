def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# 0-indexed
#
# The idea behind the solution:
#
# For len(items) == 10, there are 10! permutations. These are in ten "chunks"
# of 9!: The first 9! are permutations starting with 0, the second 9! are
# permutations starting with 1, and so on.
#
# Some arithmetic tells us that the millionth item is in the third chunk (so
# the answer permutation starts with 2) and even which index (say, M) in the
# third chunk it is -- so we can recursively apply the same technique to find
# the Mth permutation of {0,1,3,4,5,6,7,8,9} (no 2), and so on.
def get_nth_permutation(items, n):
    if len(items) == 1:
        return items[0]

    chunk_size = factorial(len(items) - 1)

    # for each chunk
    for i in range(len(items)):
        start_index = i * chunk_size
        end_index = start_index + chunk_size
        if start_index <= n < end_index:
            new_items = list(items)
            current_item = new_items.pop(i)
            new_n = n - start_index
            return current_item + get_nth_permutation(new_items, new_n)

n = 999_999 # 0-indexed
print(get_nth_permutation('0123456789', n))
