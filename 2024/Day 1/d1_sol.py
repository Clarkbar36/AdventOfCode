#PART 1
list1 = []
list2 = []
with open("p1_input.txt", "r") as file:
    for line in file:
        words = line.split()
        words = [int(x) for x in words]
        list1.append(words[0])
        list2.append(words[1])
list1.sort()
list2.sort()
diff = 0
for l1, l2 in zip(list1, list2):
    diff += abs(l1 - l2)
#PART 2
tally = {}
for item in list1:
    tally[item] = list2.count(item)
sim_score = 0
for id, tal in tally.items():
    sim_score += id * tal