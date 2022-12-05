with open('C:/Users/aclark5/PycharmProjects/AdventOfCode/Day 5/d5_stack.txt') as f:
    stack_file = f.read()

stacks_lines = stack_file.split('\n')
stacks = [list(x) for x in stacks_lines[0:8]]

stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7, stack_8, stack_9 = '', '', '', '', '', '', '', '', ''

for x in stacks:
    try:
        stack_1 += x[1]
        stack_2 += x[5]
        stack_3 += x[9]
        stack_4 += x[13]
        stack_5 += x[17]
        stack_6 += x[21]
        stack_7 += x[25]
        stack_8 += x[29]
        stack_9 += x[33]
    except IndexError:
        continue

all_stacks = [stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7, stack_8, stack_9]
all_stacks_p1 = [x.strip() for x in all_stacks]

move_file = open('C:/Users/aclark5/PycharmProjects/AdventOfCode/Day 5/d5_moves.txt', 'r')  # Set data file

for line in move_file:
    one_move = line.split('\n')
    move_info = one_move[0].split(' ')
    number_crates = int(move_info[1])
    int_from_stack = int(move_info[3]) - 1
    int_to_stack = int(move_info[5]) - 1
    for i in range(number_crates):
        from_stack = all_stacks_p1[int_from_stack][1:]
        to_stack = all_stacks_p1[int_from_stack][:1] + all_stacks_p1[int_to_stack]
        all_stacks_p1[int_from_stack] = from_stack
        all_stacks_p1[int_to_stack] = to_stack

stack_letters = [list(x)[0] for x in all_stacks_p1]
''.join(stack_letters)

all_stacks_p2 = [x.strip() for x in all_stacks]

move_file = open('C:/Users/aclark5/PycharmProjects/AdventOfCode/Day 5/d5_moves.txt', 'r')  # Set data file
for line in move_file:
    one_move = line.split('\n')
    move_info = one_move[0].split(' ')
    number_crates = int(move_info[1])
    int_from_stack = int(move_info[3]) - 1
    int_to_stack = int(move_info[5]) - 1
    from_stack = all_stacks_p2[int_from_stack][number_crates:]
    to_stack = all_stacks_p2[int_from_stack][:number_crates] + all_stacks_p2[int_to_stack]
    all_stacks_p2[int_from_stack] = from_stack
    all_stacks_p2[int_to_stack] = to_stack

stack_letters_p2 = [list(x)[0] for x in all_stacks_p2]
''.join(stack_letters_p2)
