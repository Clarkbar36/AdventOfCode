dt_file = open('C:/Users/aclark5/PycharmProjects/AdventOfCode/Day 4/d4_data.txt', 'r')  # Set data file

full_pairs = []

for line in dt_file:
    pairs = line.split(',')
    first_range = pairs[0]
    first_range_min = int(first_range.split("-")[0])
    first_range_max = int(first_range.split("-")[1])
    second_range = pairs[1]
    second_range_min = int(second_range.split("-")[0])
    second_range_max = int(second_range.split("-")[1])
    if first_range_min <= second_range_min and first_range_max >= second_range_max:
        full_pairs.append(pairs)
    elif second_range_min <= first_range_min and second_range_max >= first_range_max:
        full_pairs.append(pairs)

overlap_pairs = []

for line in dt_file:
    pairs = line.split(',')
    first_range = pairs[0]
    first_range_min = int(first_range.split("-")[0])
    first_range_max = int(first_range.split("-")[1])
    second_range = pairs[1]
    second_range_min = int(second_range.split("-")[0])
    second_range_max = int(second_range.split("-")[1])
    if first_range_min <= second_range_min and first_range_max >= second_range_min:
        overlap_pairs.append(pairs)
    elif second_range_min <= first_range_min and second_range_max >= first_range_min:
        overlap_pairs.append(pairs)
