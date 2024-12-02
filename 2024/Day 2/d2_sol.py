
def check_order(lst):
    check_increase = all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))
    check_decrease = all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))
    order = any((check_increase, check_decrease))
    check_range = all([0 < abs(lst[val] - lst[val + 1]) <= 3 for val in range(len(lst) - 1)])
    if all((order, check_range)):
        return 1
    else:
        return 0


# Part 1
with open("input.txt", "r") as file:
    i = 0
    for line in file:
        line_list = list(map(int, line.split()))
        i += check_order(line_list)


# Part 2
with open("input.txt", "r") as file:
    i = 0
    for line in file:
        line_list = list(map(int, line.split()))
        safe = False
        for val in range(len(line_list)):
            skip_list = line_list[:val] + line_list[val + 1:]
            if check_order(skip_list) == 1:
                safe = True
                break
        if safe:
            i += 1



