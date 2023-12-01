from itertools import islice

dt_file = open('C:/Users/aclark5/PycharmProjects/AdventOfCode/Day 3/d3_data.txt', 'r')  # Set data file
priority = []

#Part 1

for line in dt_file:
    firsthalf, secondhalf = line[:len(line) // 2], line[len(line) // 2:]
    priority_letter = ''.join(set(firsthalf).intersection(secondhalf))
    if priority_letter.islower():
        priority_num = ord(priority_letter) - 96
    else:
        priority_num = ord(priority_letter) - 38
    priority.append(priority_num)

sum(priority)

#Part 2

three_group_priority = []
with open('C:/Users/aclark5/PycharmProjects/AdventOfCode/Day 3/d3_data.txt', 'r') as f:
    while True:
        next_n_lines = list(islice(f, 3))
        if not next_n_lines:
            break
        common_priority = ''.join(set(next_n_lines[0]).intersection(next_n_lines[1], next_n_lines[2]))
        common_priority = common_priority.strip('\n')
        if common_priority.islower():
            three_priority_num = ord(common_priority) - 96
        elif common_priority.isupper():
            three_priority_num = ord(common_priority) - 38
        else:
            three_priority_num = 0
        three_group_priority.append(three_priority_num)
sum(three_group_priority)
