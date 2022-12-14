with open('C:/Users/aclark5/PycharmProjects/AdventOfCode/Day 13/d13_data.txt') as f:
    pairs_file = f.read().split('\n\n')

pairs = [[eval(x) for x in pair.splitlines()] for pair in pairs_file]


def compare_lists(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right

    if isinstance(left, list) and isinstance(right, list):
        for n_left, n_right in zip(left, right):
            if r := compare_lists(n_left, n_right):
                return r
        return len(left) - len(right)

    if isinstance(left, list):
        return compare_lists(left, [right])

    if isinstance(right, list):
        return compare_lists([left], right)

    assert False


ans = 0

for i, (left, right) in enumerate(pairs):
    if compare_lists(left, right) < 0:
        ans += i + 1

with open('C:/Users/aclark5/PycharmProjects/AdventOfCode/Day 13/d13_data.txt') as f:
    pair = f.read()
pairs = [eval(x) for x in pair.splitlines() if len(x) > 0]

index_of_2 = 1 # earliest index that is possible for 2
index_of_6 = 2 # earliest index that is possible for 6

# find the index for 2 and 6 using recursive search
for pair in pairs:
    if compare_lists(pair, [[2]]) < 0:
        index_of_2 += 1
        index_of_6 += 1
    elif compare_lists(pair, [[6]]) < 0:
        index_of_6 += 1

decoder_key = index_of_2 * index_of_6

print(decoder_key)