INPUT_FILE = 'd10_input.txt'
INPUT_FILE = 'd10_test_input.txt'
with open(INPUT_FILE, 'r') as f:
    L = f.read().split()

"""
Locate S character
Get the surrounding characters for current node
Check them for connectability to current node
If they connect, repeat for the process.
As nodes are traversed, replace the current character with a # symbol.

"""

# Build the matrix
pipe_matrix = []
for x in L:
    pipe_matrix.append([c for c in x])

for i, x in enumerate(pipe_matrix):
    for j, y in enumerate(x):
        if y =='S':
            sx = j
            sy = i

def check_near_positions(y,x,previous_node=None):
    lb = x-1
    rb = x+1
    tb = y-1
    bb = y+1
    if lb < 0:
        left = None
    else:
        left = pipe_matrix[y][lb]
    if rb > len(pipe_matrix[0])-1:
        right = None
    else:
        right = pipe_matrix[y][rb]
    if tb < 0:
        top = None
    else:
        top = pipe_matrix[tb][x]
    if bb > len(pipe_matrix)-1:
        bottom = None
    else:
        bottom = pipe_matrix[bb][x]
    node_set = ((left,y,lb),(right,y,rb),(top,tb,x),(bottom,bb,x))
    if not previous_node == None:
        for i, x in enumerate(node_set):
            if x == previous_node:
                node_set[i] = (None,None,None)
    return node_set
print(check_near_positions(2,0))
x = check_near_positions(2,0)
y = check_near_positions(2,1,('S',2,0))
print(y)
print(pipe_matrix)