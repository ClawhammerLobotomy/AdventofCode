from collections import namedtuple, defaultdict, deque, Counter
from itertools import chain, groupby
import math
INPUT_FILE = 'd8_input.txt'
# INPUT_FILE = 'd8_test_input.txt'

with open(INPUT_FILE, 'r') as f:
    LINE_LIST = f.read().split('\n\n')

instruction = list(LINE_LIST[0].replace('L','0').replace('R','1'))
map_nodes = defaultdict(dict)
map_codes = LINE_LIST[1].split('\n')
for m in map_codes:
    node_parts = m.split('=')
    node = node_parts[0].strip()
    node_direction = [(x[0].replace('(','').strip(),x[1].replace(')','').strip()) for x in [node_parts[1].split(',')]][0]
    map_nodes[node] = node_direction
def human_traverse():
    current_node = map_nodes['AAA']
    next_node = ''
    steps = 0
    while next_node != 'ZZZ':
        for d in instruction:
            next_node = current_node[int(d)]
            steps +=1
            current_node = map_nodes[next_node]
    print(f'Steps taken: {steps}') # 16579

def ghost_traverse(starting_nodes):
    steps = 0
    next_nodes = starting_nodes
    current_nodes = [map_nodes[x] for x in starting_nodes]
    while not all(nn[-1] == 'Z' for nn in next_nodes):# next_node[-1] != 'Z':
        for d in instruction:
            next_nodes = [x[int(d)] for x in current_nodes]
            steps +=1
            current_nodes = [map_nodes[x] for x in next_nodes]
    return steps            
            # yield steps
"""
Get a grouping of starting nodes
Send all 
"""
starting_nodes = [x for x in map_nodes.keys() if x[-1] == 'A']
test = ghost_traverse(starting_nodes)
# for x in test:
    # print(x)
print(test)