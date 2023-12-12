from collections import defaultdict
from ast import literal_eval as make_tuple
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
    node_direction = [(x[0].strip(),x[1].strip()) for x in [node_parts[1][2:-1].split(',')]][0]
    map_nodes[node] = node_direction
def human_traverse(start_node, end_node):
    steps = 0
    next_node = start_node
    current_node = map_nodes[next_node]
    while next_node != end_node:
        for d in instruction:
            next_node = current_node[int(d)]
            steps +=1
            current_node = map_nodes[next_node]
    return steps

def ghost_traverse(start_node):
    steps = 0
    next_node = start_node
    current_node = map_nodes[next_node]
    while not next_node[-1] =='Z':
        for d in instruction:
            next_node = current_node[int(d)]
            steps +=1 
            current_node = map_nodes[next_node]
            yield(steps, next_node)

starting_nodes = [x for x in map_nodes.keys() if x[-1] == 'A']
human_steps = human_traverse('AAA','ZZZ')
most_steps = math.lcm(*[e[0] for (s,*m,e) in [ghost_traverse(x) for x in starting_nodes]])


print(f'Human steps taken: {human_steps}') # 16579
print(f'Ghost steps taken: {most_steps}')
# 12927600769609 = too low??? Mistyped it I guess. This is correct.
