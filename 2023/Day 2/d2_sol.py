from collections import defaultdict
ll = [x for x in open("2023/Day 2/d2_input.txt").read().strip().split('\n')]

p1 = 0
p2 = 0
for l in ll:
    gameid = int(l.split(":")[0].split(" ")[1]) # find gameid
    l = l.split(":")[1] # split off to just rounds
    possible = True # set possible to true
    mincnts = defaultdict(int) # create deafult dict
    for s in l.split(";"): # split to each round
        cnts = defaultdict(int) # set counts to int
        for rev in s.split(", "): # split the round by cubes pulled
            rev = rev.strip() # strip blank space
            cnts[rev.split(" ")[1]]+=int(rev.split(" ")[0]) # put the color and cube amount in deafultdict
        for k,v in cnts.items():
            mincnts[k] = max(mincnts[k], v) # find max of each color for the game
        if not (cnts["red"] <= 12 and cnts["green"] <= 13 and cnts["blue"] <= 14): # compare
            possible=False
    if possible:
        p1 += gameid # add gameid
    p2 += mincnts["red"]*mincnts["green"]*mincnts["blue"]
print(p1)
print(p2)