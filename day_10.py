from collections import namedtuple

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
pipeNode = namedtuple('pipeNode',['character','ypos','xpos','connections','connects'])

# Build the matrix
PIPE_MATRIX = []
for x in L:
    PIPE_MATRIX.append([c for c in x])

# connection_dict = {
#     'J':('RIGHT','BOTTOM'),
#     'F':('TOP','LEFT'),
#     '|':('TOP','BOTTOM'),
#     'L':('BOTTOM','LEFT'),
#     '-':('LEFT','RIGHT'),
#     '7':('RIGHT','TOP'),
#     '.':'GROUND',
#     'S':('LEFT','RIGHT','TOP','BOTTOM'),
#     '#':'USED'
# }
connection_dict = {
    'F':('RIGHT','BOTTOM'),
    'J':('TOP','LEFT'),
    'L':('RIGHT','TOP'),
    '7':('BOTTOM','LEFT'),
    '-':('LEFT','RIGHT'),
    '|':('TOP','BOTTOM'),
    '.':('GROUND'),
    'S':('START'),
    '#':('USED')
}

class pipeNode:
    def __init__(self,c,y,x):
        self.c = c
        self.y = y
        self.x = x
        self.connections = connection_dict[self.c]
        self.visited = False
        # self.surrounding_nodes_get()
    def surrounding_nodes_get(self):
        lb = self.x-1
        rb = self.x+1
        tb = self.y-1
        bb = self.y+1
        if lb < 0:
            ln = None
        else:
            ln = PIPE_MATRIX[self.y][lb]
        if rb > len(PIPE_MATRIX[0])-1:
            rn = None
        else:
            rn = PIPE_MATRIX[self.y][rb]
        if tb < 0:
            tn = None
        else:
            tn = PIPE_MATRIX[tb][self.x]
        if bb > len(PIPE_MATRIX)-1:
            bn = None
        else:
            bn = PIPE_MATRIX[bb][self.x]
        node_set = [ln,rn,tn,bn]
        self.next_node = [n for n in node_set if n != None and any(y in self.connections for y in n.connections)]

def connection_check(node,type):
    if type in node:
        return True
    return False

def find_start(PIPE_MATRIX):
    for i, x in enumerate(PIPE_MATRIX):
        for j, y in enumerate(x):
            PIPE_MATRIX[i][j] = pipeNode(y,i,j)
            # if y =='S':
            #     sx = j
            #     sy = i
            #     return pipeNode(y,i,j)

def check_near_positions(starting_node,previous_node=None):
    y = starting_node.y
    x = starting_node.x
    lb = x-1
    rb = x+1
    tb = y-1
    bb = y+1
    if lb < 0:
        left_node = None
    else:
        left = PIPE_MATRIX[y][lb]
        left_node = pipeNode(left,y,lb,'LEFT')
        # PIPE_MATRIX[y][lb] = '#'
    if rb > len(PIPE_MATRIX[0])-1:
        right_node = None
    else:
        right = PIPE_MATRIX[y][rb]
        right_node = pipeNode(right,y,rb,'RIGHT')
        # PIPE_MATRIX[y][rb] = '#'
    if tb < 0:
        top_node = None
    else:
        top = PIPE_MATRIX[tb][x]
        top_node = pipeNode(top,tb,x,'TOP')
        # PIPE_MATRIX[tb][x] = '#'
    if bb > len(PIPE_MATRIX)-1:
        bottom_node = None
    else:
        bottom = PIPE_MATRIX[bb][x]
        bottom_node = pipeNode(bottom,bb,x,'BOTTOM')
        # PIPE_MATRIX[bb][x] = '#'
    
    node_set = [left_node,right_node,top_node,bottom_node]
    connecting_nodes = [x for x in node_set if x != None and len(x.connections) == 2]
    # if not previous_node == None:
    #     for i, x in enumerate(node_set):
    #         if x == previous_node:
    #             node_set[i] = None
    return connecting_nodes
# print(check_near_positions(2,0))
start = find_start(PIPE_MATRIX)
for x in PIPE_MATRIX:
    for y in x:
        y.surrounding_nodes_get()
i = 0
node_list = check_near_positions(start)
while "S" not in [x.c for x in node_list] and node_list != []:
    print(i)
    i += 1
    print(node_list)
    for n in node_list:
        if n == None:
            continue
        if n.c == 'S':
            print('returned back to start in {i} iterations')
            break
        node_list = check_near_positions(n)
        print(n, check_near_positions(n))
        
# y = check_near_positions(2,1,('S',2,0))
# print(y)
print(PIPE_MATRIX)