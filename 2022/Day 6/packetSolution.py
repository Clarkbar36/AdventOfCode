with open('C:/Users/aclark5/PycharmProjects/AdventOfCode/Day 6/d6_data.txt') as f:
    packet_file = f.read()

# Part 1
for i in range(0, len(packet_file)):
    four_packet = packet_file[i:i + 4]
    if len(set(four_packet)) == 4:
        print(i + 4)
        break
    else:
        pass

# Part 2
for i in range(0, len(packet_file)):
    four_packet = packet_file[i:i + 14]
    if len(set(four_packet)) == 14:
        print(i + 14)
        break
    else:
        pass