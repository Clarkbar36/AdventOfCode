import pandas as pd
from math import prod

df = pd.read_fwf('C:/Users/aclark5/PycharmProjects/AdventOfCode/Day 8/d8_data.txt', widths=[1] * 99, header=None)

how_many_seen = 0
trees = pd.DataFrame()

for r in range(df.shape[0]):  # iterate over rows
    for c in range(df.shape[1]):  # iterate over columns
        tree_height = df.at[r, c]  # get cell value

        # row right [r:r+1 ,c+1:]
        right_max = int(df.iloc[r:r + 1, c + 1:].max(axis=1).fillna(0))

        # row left [r:r+1 ,:c]
        left_max = int(df.iloc[r:r + 1, :c].max(axis=1).fillna(0))

        # column down [r:,c]
        down_max = df.iloc[r + 1:, c].max()
        if type(down_max) == float:
            down_max = 0

        # column up [:r,c]
        up_max = df.iloc[:r, c].max()
        if type(up_max) == float:
            up_max = 0

        if tree_height == 0 and 0 < c < 98 and 0 < r < 98:
            tree_height = 'X'
        elif 0 in [up_max, down_max, right_max, left_max]:
            how_many_seen += 1
            tree_height = 'O'
        elif tree_height > up_max or tree_height > down_max or tree_height > right_max or tree_height > left_max:
            how_many_seen += 1
            tree_height = 'O'
        else:
            tree_height = 'X'

        trees.at[r, c] = tree_height

# dataframe was the wrong choice, using Olvier Ni's solution
with open('C:/Users/aclark5/PycharmProjects/AdventOfCode/Day 8/d8_data.txt') as f:
    grid = f.read().splitlines()
    ans = []

    for r, row in enumerate(grid):
        for c, tree in enumerate(row):
            ans.append([0, 0, 0, 0])

            for j in range(c - 1, -1, -1):
                ans[-1][0] += 1
                if grid[r][j] >= tree:
                    break

            for i in range(r - 1, -1, -1):
                ans[-1][1] += 1
                if grid[i][c] >= tree:
                    break

            for j in range(c + 1, len(row)):
                ans[-1][2] += 1
                if grid[r][j] >= tree:
                    break

            for i in range(r + 1, len(grid)):
                ans[-1][3] += 1
                if grid[i][c] >= tree:
                    break

    max(prod(x) for x in ans)
