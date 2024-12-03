import re

# Part 1
with open("input", "r") as file:
    contents = file.read()
    mul_pattern = r'mul\((\d+),\s*(\d+)\)'

    p1_matches = re.findall(mul_pattern, contents)

i = 0
for mul in p1_matches:
    i += int(mul[0]) * int(mul[1])
print(f"part 1 answer: {i}")

# Part 2
enabled_string = 'do()'
disabled_string = 'don\'t()'

with open("input", "r") as file:
    contents = file.read()

    mul_pattern = r'mul\((\d+),\s*(\d+)\)'
    enabled_pattern = re.compile(f"{re.escape(disabled_string)}.*?{re.escape(enabled_string)}", re.DOTALL)
    
    cleaned_content = re.sub(enabled_pattern, f"{disabled_string}{enabled_string}", contents)
    p2_matches = re.findall(mul_pattern, cleaned_content)

i = 0
for mul in p2_matches:
    i += int(mul[0]) * int(mul[1])
print(f"part 2 answer: {i}")

