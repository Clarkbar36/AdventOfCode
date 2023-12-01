class lol(tuple):
    def __add__(self, other):
        return lol(a + b for a, b in zip(self, other))

    def __sub__(self, other):
        return lol(a - b for a, b in zip(self, other))


with open('C:/Users/aclark5/PycharmProjects/AdventOfCode/Day 9/d9_data.txt') as f:
    move_file = f.read().splitlines()

DIRS = {
    "R": lol((1, 0)),
    "L": lol((-1, 0)),
    "U": lol((0, 1)),
    "D": lol((0, -1)),
}


def move(h, t):
    diff = lol(min(1, max(-1, x)) for x in h - t)
    if h - t == diff:
        return t
    return t + diff


def p1(f):
    h = t = lol((0, 0))
    pos = set()

    for line in move_file:
        dir, step = line.split()

        for i in range(int(step)):
            h += DIRS[dir]
            t = move(h, t)
            pos.add(t)

    return len(pos)
