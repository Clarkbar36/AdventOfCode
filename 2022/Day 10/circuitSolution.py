dt_file = open('C:/Users/aclark5/PycharmProjects/AdventOfCode/Day 10/d10_data.txt', 'r')  # Set data file

cycle = 0
value = 1
signal_strength = {}
cycle_check = list(range(20, 221, 40))


def add_and_check():
    global cycle, value
    cycle += 1
    if cycle in cycle_check:
        signal_strength[str(cycle)] = cycle * value


for line in dt_file:
    sline = line.split()
    if sline[0] == "noop":
        add_and_check()
        print(sline, " = ", str(cycle) + " : " + str(value))
    else:
        add_and_check()
        print(sline, " = ", str(cycle) + " : " + str(value))
        add_and_check()
        value += int(sline[1])
        print(sline, " = ", str(cycle) + " : " + str(value))

sum(signal_strength.values())


## Part 2
dt_file = open('C:/Users/aclark5/PycharmProjects/AdventOfCode/Day 10/d10_data.txt', 'r')  # Set data file
x = 1
cycle = 0
crt = []
for row in range(0, 6):
    crt.append([])
    for col in range(0, 40):
        crt[row].append('.')


def show():
    global crt
    for row in range(0, 6):
        print(''.join(crt[row]))


def tick():
    global crt, cycle, x
    row = cycle // 40
    col = cycle % 40
    if abs(x - col) <= 1:
        print(str(x), str(col))
        crt[row][col] = '#'
    cycle += 1


for line in dt_file:
    line = line.rstrip()
    if line == 'noop':
        tick()
    else:
        _, addx = line.split(' ')
        tick()
        tick()
        x += int(addx)

show()