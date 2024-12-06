with open('d6_input.txt', 'r') as f:
    x = f.read().strip().split()
TEST = False
TEST1 = 41
PART1 = 5067
if TEST:
    x = [
        "....#.....",
        ".........#",
        "..........",
        "..#.......",
        ".......#..",
        "..........",
        ".#..^.....",
        "........#.",
        "#.........",
        "......#..."
    ]
x = [list(i) for i in x]


turn_right = {
    '^':'<',
    '>':'^',
    'V':'>',
    '<':'V',
    '.':'.',
    '#':'#',
    'X':'X'
}
def array_rotate(input_list):
    new_list = []
    for i in range(len(input_list[0])):
        new_list.insert(0,[x[i].replace(x[i],turn_right[x[i]]) for x in input_list])
    return new_list
r = array_rotate(x)
d = array_rotate(r)
l = array_rotate(d)
# print(r)



"""
find position index x,y
determine facing, replace current position with an X
up:
    check each x index for reducing y indices until a # symbol is found. replace all dots with X
right: 
    check same y index for increasing x indices until a # symbol is found, replacing dots with X
down:
    check each x index for increasing y indices until a # symbol is found. replace all dots with X
left:
    check same y index for deccreasing x indices until a # symbol is found, replacing dots with X
follow the paths until a # symbol is reached or an array bound is reached.
If the array bound is reached, we've hit the end.
"""

map_edge = False
def move_up(input_map, x, y):
    global map_edge
    obstacle = False
    for i, c in enumerate(input_map[y::-1]):
        # print(c)
        if c[x] == '#':
            obstacle = True
            input_map[y-len(input_map)+1][x] = '>'
            break
        c[x] = 'X'
        y -= 1
    if not obstacle:
        print('Reached map edge')
        map_edge = True
    return x, i, facing['>']
def move_right():...
def move_left():...
def move_down():...
facing = {
    '^':move_up,
    '>':move_right,
    '<':move_left,
    'V':move_down
}
def get_pos(input_map):
    for i, c in enumerate(input_map):
        for j, r in enumerate(c):
            if r in facing.keys():
                f = (j, i, facing[r])
                # r = 'X'
                return f

def count_x(input_map):
    t = ''.join([''.join(r) for r in input_map])
    xcount = [c for c in list(t) if c == 'X']
    return len(xcount)

xpos,ypos,func = get_pos(x)

while not map_edge:
    xpos,ypos,func = func(x,xpos,ypos)
    if map_edge:
        break
    x = array_rotate(x)
    xpos,ypos,func = get_pos(x)
    # print(xpos,ypos)
spaces = count_x(x)
print(f'Part 1: {spaces}')
if TEST:
    assert(spaces == TEST1)
else:
    assert(spaces == PART1)
print('done')