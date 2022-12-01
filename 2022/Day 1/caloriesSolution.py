import pandas as pd

dt_file = open('C:/Users/aclark5/PycharmProjects/AdventOfCode/2022/Day 1/d1_data.txt', 'r')
elf_num = 1
elf_calories = []
all_elf_cals = pd.DataFrame({'Elf': pd.Series(dtype='str'),
                             'Total_Calories': pd.Series(dtype='int')})
for line in dt_file:
    if line == '\n':
        elf = 'elf ' + str(elf_num)
        total_calories = sum(elf_calories)
        row = [elf, total_calories]
        all_elf_cals.loc[len(all_elf_cals)] = row
        elf_num += 1
        elf_calories = []
    else:
        elf_calories.append(int(line))

max_elf = all_elf_cals[all_elf_cals['Total_Calories'] == all_elf_cals['Total_Calories'].max()]

top_3_calories = all_elf_cals.nlargest(3, 'Total_Calories')['Total_Calories'].sum()



