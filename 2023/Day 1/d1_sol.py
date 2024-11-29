import csv
import os
import re
from math import inf

calibrations = []

with open("2023/Day 1/d1_input.csv", mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        numsInString = []
        row_str = ''.join(row)
        for index, char in enumerate(row_str):
            # Checking if char is numeric
            if char.isdigit():
                numsInString.append(char)
        if len(numsInString) == 1:
            numsInString.append(numsInString[0])

        lineInt = int(''.join(numsInString[::len(numsInString) - 1]))
        calibrations.append(lineInt)

print(sum(calibrations))


# part 2
nums = '0 zero 1 one 2 two 3 three 4 four 5 five 6 six 7 seven 8 eight 9 nine'.split()

ans = 0

with open("2023/Day 1/d1_input.csv") as f:
    for row in f:
        rsting = row
        first = min(nums, key=lambda x: row.index(x) if x in row else inf)
        last =  min(nums, key=lambda x: row[::-1].index(x[::-1]) if x in row else inf)
        ans += nums.index(first) // 2 * 10 + nums.index(last) // 2


0 // 2 * 10 + 5 // 2 = 0 + 2 * 10 + 2
