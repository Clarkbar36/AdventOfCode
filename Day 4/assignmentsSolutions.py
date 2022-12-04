dt_file = open('C:/Users/aclark5/PycharmProjects/AdventOfCode/Day 4/d4_data.txt', 'r')  # Set data file

full_pairs = []

for message in dt_file:
    lines = message.split(',')
    first_range = lines[0]
    first_range_min = int(first_range.split("-")[0])
    first_range_max = int(first_range.split("-")[1])
    second_range = lines[1]
    second_range_min = int(second_range.split("-")[0])
    second_range_max = int(second_range.split("-")[1])
    if first_range_min <= second_range_min and first_range_max >= second_range_max:
        full_pairs.append(lines)
    elif second_range_min <= first_range_min and second_range_max >= first_range_max:
        full_pairs.append(lines)

overlap_pairs = []

for message in dt_file:
    lines = message.split(',')
    first_range = lines[0]
    first_range_min = int(first_range.split("-")[0])
    first_range_max = int(first_range.split("-")[1])
    second_range = lines[1]
    second_range_min = int(second_range.split("-")[0])
    second_range_max = int(second_range.split("-")[1])
    if first_range_min <= second_range_min and first_range_max >= second_range_min:
        overlap_pairs.append(lines)
    elif second_range_min <= first_range_min and second_range_max >= first_range_min:
        overlap_pairs.append(lines)
