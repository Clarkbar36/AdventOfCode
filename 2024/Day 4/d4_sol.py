word = 'XMAS'
grid = []
with open("input", "r") as file:
    for line in file:
        grid.append(line)

# part 1
rows = len(grid)
cols = len(grid[0])
directions = [
    (-1, 0),  # Up
    (1, 0),  # Down
    (0, -1),  # Left
    (0, 1),  # Right
    (-1, -1),  # Up-Left
    (-1, 1),  # Up-Right
    (1, -1),  # Down-Left
    (1, 1)  # Down-Right
]
i = 0

for rowindex, line in enumerate(grid):
    for colindex, val in enumerate(line):
        if val != word[0]:
            continue

        # Check each direction
        for dr, dc in directions:
            new_row = rowindex
            new_col = colindex
            match = True

            for step in range(1, len(word)):
                new_row += dr
                new_col += dc

                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                    match = False
                    break

                if grid[new_row][new_col] != word[step]:
                    match = False
                    break

            if match:
                i += 1

        # Output all matches
print(f"Total matches found: {i}")

# Part 2
grid = []
with open("input", "r") as file:
    for line in file:
        grid.append(line)
word = 'MAS'

rows = len(grid)
cols = len(grid[0])
matches = 0

for rowindex, line in enumerate(grid):
    for colindex, val in enumerate(line):
        if val != 'A':
            continue

        # First diagonal (Up-Left to Down-Right)
        m_row1, m_col1 = rowindex - 1, colindex - 1  # up-left
        s_row1, s_col1 = rowindex + 1, colindex + 1  # down-right

        # Reverse First diagonal (Down-Left to Up-Right)
        m_row2, m_col2 = rowindex + 1, colindex - 1  # down-left
        s_row2, s_col2 = rowindex - 1, colindex + 1  # up-right

        found_valid_diagonal_1 = False
        if 0 <= m_row1 < rows and 0 <= m_col1 < cols and 0 <= s_row1 < rows and 0 <= s_col1 < cols:
            if (grid[m_row1][m_col1] == word[0] and grid[s_row1][s_col1] == word[2]) or (
                    grid[m_row1][m_col1] == word[2] and grid[s_row1][s_col1] == word[0]):
                found_valid_diagonal_1 = True

        found_valid_diagonal_2 = False
        if 0 <= m_row2 < rows and 0 <= m_col2 < cols and 0 <= s_row2 < rows and 0 <= s_col2 < cols:
            if (grid[m_row2][m_col2] == word[0] and grid[s_row2][s_col2] == word[2]) or (
                    grid[m_row2][m_col2] == word[2] and grid[s_row2][s_col2] == word[0]):
                found_valid_diagonal_2 = True

        if found_valid_diagonal_1 and found_valid_diagonal_2:
            matches += 1
print(f"Total cross matches found: {matches}")
