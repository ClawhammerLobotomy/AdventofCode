import math
INPUT_FILE = 'd6_input.txt'
# INPUT_FILE = 'd6_test_input.txt'

with open(INPUT_FILE, 'r') as f:
    LINE_LIST = f.read()

times = LINE_LIST.split('\n')[0].split(':')[1].split()
distances = LINE_LIST.split('\n')[1].split(':')[1].split()
p1races = [(int(t),int(d)) for t,d in list(zip(times,distances))]
p2races = [(int(''.join(times)),int(''.join(distances)))]
def margin_find(races):
    winning_races = []
    for r in races:
        win_count = 0
        t,d = r
        for bt in range(t+1):
            dt = (t-bt) * bt
            if dt > d:
                win_count += 1
        winning_races.append(win_count)
    return math.prod(winning_races)

print('Part 1:',margin_find(p1races)) # 138915
print('Part 2:',margin_find(p2races)) # 27340847