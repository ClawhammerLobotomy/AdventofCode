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
orig_map = list(x)
# orig_map = [list(i) for i in orig_map]
x = [list(i) for i in x]


turn_right = {
    '^':'<',
    '>':'^',
    'V':'>',
    '<':'V',
    '.':'.',
    '#':'#',
    'X':'X',
    'O':'O'
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
moving = '^'
loops_tried = []
exit_position = None
obstacle_pos = None
def move_up(input_map, x, y, do_loops=True):
    global map_edge, loop_try, loops_tried, obstacle_pos
    obstacle = False
    for i, c in enumerate(input_map[y::-1]):
        # print(c)
        if c[x] in ('#','O'):
            obstacle = True
            input_map[y-len(input_map)+1][x] = '>'
            break
        # if '#' in c[x::] and (x,y,moving) not in loops_tried and not loop_try and do_loops:
        if '#' in c[x::] and (x,y) not in loops_tried and not loop_try and do_loops:
            obstacle = True
            loop_try = True
            if y == 0:
                input_map[y][x] = 'O'
                # obstacle_pos = (x,y,moving)
                obstacle_pos = (x,y)
                input_map[y+1][x] = '>'
            else:
                input_map[y-len(input_map)-1][x] = 'O'
                # obstacle_pos = (x,y-len(input_map)-1,moving)
                obstacle_pos = (x,y-len(input_map)-1)
                input_map[y-len(input_map)][x] = '>'
            # loops_tried.append((x,y,moving))
            loops_tried.append((x,y))

            # obstacle_pos = 
            break
        c[x] = 'X'
        y -= 1 if y > 0 else 0
    if not obstacle:
        # print('Reached map edge')
        map_edge = True
        # return (x,y,moving)
        return (x,y)
    # return x, i, facing['>']
    return x, i
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

loop_indexes = []
loop_obstacles = []
loop_try = False
looped = False
def map_solve(input_map,first_solve=False):
    global looped, moving, loop_indexes
    
    do_loops = True if not first_solve else False
    xpos,ypos,func = get_pos(input_map)
    visited = []
    while not map_edge:
        # xpos,ypos,func = func(input_map,xpos,ypos,do_loops)
        xpos,ypos = func(input_map,xpos,ypos,do_loops)
        if map_edge:
            while moving != '^': # Get map back into correct orientation for easier visualization
                input_map = array_rotate(input_map)
                moving = turn_right[moving]
            break
        if (xpos,ypos,moving) in visited:
            print('Loop detected')
            # looped = True
            loop_indexes.append((xpos,ypos,moving))
            loop_obstacles.append(obstacle_pos)
            # (x,y,moving)
            break
        # if (xpos,ypos,moving) in loop_indexes:
        #     # looped = False
        #     continue
        visited.append((xpos,ypos,moving))
        input_map = array_rotate(input_map)
        moving = turn_right[moving]
        xpos,ypos,func = get_pos(input_map)
        # print(xpos,ypos)
    return (xpos,ypos) if map_edge else input_map
loop_count = 0
while not map_edge:
    exit_position = map_solve(x, first_solve=True)
while not exit_position in loop_obstacles or not exit_position in loops_tried:

    map_edge = False
    loop_try = False
    x = [list(i) for i in orig_map]
    x = map_solve(x)
    # if x == exit_position:
    #     break

# loops = len(list(set(loop_indexes)))
loops = len(loop_indexes)
loops_2 = len(loop_obstacles)

# spaces = count_x(x)
# print(f'Part 1: {spaces}')
print(f'Part 2: {loops}')
# if TEST:
#     assert(spaces == TEST1)
# else:
#     assert(spaces == PART1)

"""
For part 2, need to find a way to look at the X values and see if any of them can be made into rectangles by replacing an X with an obstacle
"""
print('done')