with open("C:/Users/aclark5/PycharmProjects/AdventOfCode/Day 7/cody_test.txt", "r") as f:
    dt_file = f.read()

folder_sizes = {}
folder_path = []

lines = dt_file.splitlines()
for line in lines:
    input = line.split()
    if input[0] == "$":
        if input[1] == "cd":
            if input[2] == "..":
                folder_path = folder_path[:-1]
            elif input[2] == "/":
                folder_path = ["/"]
            else:
                folder_path.append(input[2])
    else:
        if input[0] != "dir":
            current_path = ""
            for folder in folder_path:
                if current_path != "/" and folder != "/":
                    current_path += "/"
                current_path += folder
                folder_sizes[current_path] = folder_sizes.get(current_path, 0) + int(input[0])

# Part 1
print(sum(value for name, value in folder_sizes.items() if value < 100000))


t = {key: folder_sizes[key] for key in folder_sizes if folder_sizes[key] < 100_000}

# Part 2
needed_space = 30000000 - (70000000 - folder_sizes.get("/"))
print(min(value for name, value in folder_sizes.items() if value >= needed_space))