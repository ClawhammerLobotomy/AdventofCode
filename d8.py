from itertools import combinations
with open('d8_input.txt', 'r') as f:
    x = f.read().strip()
TEST = False
TEST1 = 14
PART1 = 244
nodes = list(set(x))
x = x.split()
if TEST:
    x = [
    "............",
    "........0...",
    ".....0......",
    ".......0....",
    "....0.......",
    "......A.....",
    "............",
    "............",
    "........A...",
    ".........A..",
    "............",
    "............"
    ]
    nodes = ['0','A']

"""
Find first character position.
Find all pair positions.
Calculate distance between pair.
Calculate 2 antinodes. 
Check if the antinode position is within the bounds of the list.
"""
xbounds = len(x[0])
ybounds = len(x)


def find_pairs(input_list, chr):
    for i, r in enumerate(input_list):
        for j, c in enumerate(r):
            if c == chr:
                yield (i, j)

def valid_check(antinode):
    if antinode[0] < 0 or antinode[0] >= xbounds:
        return 0
    if antinode[1] < 0 or antinode[1] >= ybounds:
        return 0
    return 1
def find_anti(pair):
    p1x, p1y = pair[0]
    p2x, p2y = pair[1]
    xdist = p2x-p1x
    ydist = p2y-p1y
    anti1 = (p1x-xdist, p1y-ydist)
    anti2 = (p2x+xdist, p2y+ydist)
    return (anti1, anti2)


valid_antis = []

for n in nodes:
    if n == '.' or n == '\n':
        continue
    print(f'Finding pairs for {n}')
    t = find_pairs(x, n)
    comb = combinations(t, 2)
    for c in comb:
        print(f'Finding antis')
        antis = find_anti(c)
        for a in antis:
            if valid_check(a):
                if a not in valid_antis:
                    print(f'New valid antinode found for {n} at {a}')
                    valid_antis.append(a)
                else:
                    print(f'Existing valid antinode found for {n} at {a}. Not adding to list.')
            else:
                print(f'Invalid antinode for {n} at {a}')


anti_count = len(valid_antis)
# print(valid_antis)
# 2601 - Too high, forgot to omit the . and \n characters from pair finding.
# 251 - Still too high. - Upper bounds off by one using len(x)
print(f"Part 1: {anti_count}") 
