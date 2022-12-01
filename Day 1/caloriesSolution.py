import pandas as pd

dt_file = open('C:/Users/aclark5/PycharmProjects/AdventOfCode/2022/Day 1/d1_data.txt', 'r') # Set data file
elf_num = 1 # set elf number
elf_calories = [] # blank list to add calories to
all_elf_cals = pd.DataFrame({'Elf': pd.Series(dtype='str'), # blank df to compile all elf totals
                             'Total_Calories': pd.Series(dtype='int')})
for line in dt_file:
    if line == '\n':
        elf = 'elf ' + str(elf_num) # give elf id
        total_calories = sum(elf_calories) # sum all calories gathered before blank line
        row = [elf, total_calories] # gather up elf id and total calories into a row
        all_elf_cals.loc[len(all_elf_cals)] = row # insert into dataframe
        elf_num += 1 # add 1 to elf id
        elf_calories = [] # clear out elf calories list
    else:
        elf_calories.append(int(line)) # add calories to list

max_elf = all_elf_cals[all_elf_cals['Total_Calories'] == all_elf_cals['Total_Calories'].max()] # find elf with max calories

top_3_calories = all_elf_cals.nlargest(3, 'Total_Calories')['Total_Calories'].sum() # add up the top 3 elves calories



