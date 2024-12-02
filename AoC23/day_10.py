from collections import namedtuple

INPUT_FILE = 'd10_input.txt'
# INPUT_FILE = 'd10_test_input.txt'
with open(INPUT_FILE, 'r') as f:
    L = f.read().split()

"""
Locate S character
Get the surrounding characters for current node
Check them for connectability to current node
If they connect, repeat for the process.
As nodes are traversed, replace the current character with a # symbol.
"""

"""
Start with S
Replace with valid pipe to record the valid connectors
Record the position of Start to know when we get back

Add current position to list of "Seen"
Check 4 nodes around current.
Compare if they can be connected to current node.
If they can, Pick one to use that isn't in the "SEEN" list
repeat for this node
"""

# pipeNode = namedtuple('pipeNode',['character','ypos','xpos','connections','connects'])

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
    'J':('RIGHT','BOTTOM'),
    'F':('TOP','LEFT'),
    '7':('RIGHT','TOP'),
    'L':('BOTTOM','LEFT'),
    '-':('LEFT','RIGHT'),
    '|':('TOP','BOTTOM'),
    '.':('GROUND'),
    'S':('START'),
    '#':('USED')
}

travel_directions = {
    'F':('RIGHT','BOTTOM'),
    'J':('TOP','LEFT'),
    'L':('RIGHT','TOP'),
    '7':('BOTTOM','LEFT'),
    '-':('LEFT','RIGHT'),
    '|':('TOP','BOTTOM'),
    '.':('GROUND'),
    'S':('RIGHT','BOTTOM','TOP','LEFT')
}

VALID_RIGHT = ('7','J','-')
VALID_LEFT = ('L','-','F')
VALID_TOP = ('|','7','F')
VALID_BOTTOM = ('|','L','J')

class pipeNode:
    def __init__(self,c,y,x):
        self.c = c
        self.y = y
        self.x = x
        self.connections = connection_dict[self.c]
        self.visited = False
        self.travel_directions = travel_directions[self.c]
        self.valid = False
        self.start = False
        if self.c == 'S':
            self.start = True


    def surrounding_nodes_get(self):
        lb = self.x-1
        rb = self.x+1
        tb = self.y-1
        bb = self.y+1
        if lb < 0:
            self.ln = None
        else:
            self.ln = PIPE_MATRIX[self.y][lb]
            # if any(x in self.travel_directions for x in ln.connections):
            if self.ln.c in VALID_LEFT:
                self.ln.valid = True
        if rb > len(PIPE_MATRIX[0])-1:
            self.rn = None
        else:
            self.rn = PIPE_MATRIX[self.y][rb]
            # if any(x in self.travel_directions for x in rn.connections):
            if self.rn.c in VALID_RIGHT:
                self.rn.valid = True
        if tb < 0:
            self.tn = None
        else:
            self.tn = PIPE_MATRIX[tb][self.x]
            # if any(x in self.travel_directions for x in tn.connections):
            if self.tn.c in VALID_TOP:
                self.tn.valid = True
        if bb > len(PIPE_MATRIX)-1:
            self.bn = None
        else:
            self.bn = PIPE_MATRIX[bb][self.x]
            # if any(x in self.travel_directions for x in bn.connections):
            if self.bn.c in VALID_BOTTOM:
                self.bn.valid = True


    def start_replace(self):
        directions = []
        if any(x == self.rn.c for x in VALID_RIGHT if self.rn):
            directions.append('RIGHT')
        if any(x == self.ln.c for x in VALID_LEFT if self.ln):
            directions.append('LEFT')
        if any(x == self.tn.c for x in VALID_TOP if self.tn):
            directions.append('TOP')
        if any(x == self.bn.c for x in VALID_BOTTOM if self.bn):
            directions.append('BOTTOM')
        for k,d in travel_directions.items():
            if set(directions) == set(d):
                self.c = k


def connection_check(node,type):
    if type in node:
        return True
    return False


def classify_nodes(PIPE_MATRIX):
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
classify_nodes(PIPE_MATRIX)

for x in PIPE_MATRIX:
    for y in x:
        y.surrounding_nodes_get()
starting_node = [j for x in PIPE_MATRIX for j in x if j.start][0]
starting_node.start_replace()
starting_node.travel_directions = travel_directions[starting_node.c]

seen = []
def next_node(n,previous_node_pos):
    path = [x for x in n.travel_directions if x != previous_node_pos][0]
    match path:
        case 'RIGHT':
            nn = n.rn
            pnp = 'LEFT'
        case 'LEFT':
            nn = n.ln
            pnp = 'RIGHT'
        case 'BOTTOM':
            nn = n.bn
            pnp = 'TOP'
        case 'TOP':
            nn = n.tn
            pnp = 'BOTTOM'
    return nn, pnp

nn,pnp = next_node(starting_node,starting_node.travel_directions[1])
i = 1
while starting_node not in seen:
    nn, pnp = next_node(nn,pnp)
    seen.append(nn)
    i += 1
    # print(nn.c)
    # print(i)

number_of_steps = i//2
print(number_of_steps) # 7086 part 1