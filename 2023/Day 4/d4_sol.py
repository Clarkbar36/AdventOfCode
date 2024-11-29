from functools import reduce

ans = 0
with open("2023/Day 4/d4_input.txt") as f:
    for row in f:
        scratch = row.split('|')
        winning_nums = scratch[0].split(':')[1].split()
        your_nums = scratch[1].split()
        res = reduce(lambda x, y: x + winning_nums.count(y), set(your_nums), 0)
        if res != 0:
            ans += pow(2, (res - 1))
