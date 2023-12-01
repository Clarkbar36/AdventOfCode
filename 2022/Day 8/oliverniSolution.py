from math import prod
with open('C:/Users/aclark5/PycharmProjects/AdventOfCode/Day 8/d8_data.txt') as f:

    grid = f.read().splitlines()
    ans = 0
    #trees = pd.DataFrame()
    for ti, row in enumerate(grid):
        for tj, tree in enumerate(row):

            ans += (
                all(grid[ti][j] < tree for j in range(0, tj))
                or all(grid[ti][j] < tree for j in range(tj + 1, len(row)))
                or all(grid[i][tj] < tree for i in range(0, ti))
                or all(grid[i][tj] < tree for i in range(ti + 1, len(grid)))
            )


for j in range(tj - 1, -1, -1):
    print(j)
ti = 5
tj = 78