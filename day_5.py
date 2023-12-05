from collections import namedtuple
INPUT_FILE = 'd5_input.txt'
INPUT_FILE = 'd5_test_input.txt'

with open(INPUT_FILE, 'r') as f:
    LINE_LIST = f.read()

# class Mapping():
#     def __init__(self):
#         self.
Mapping = namedtuple('Mapping',['map_type','source_start','destination_start','range_length'])
parts = LINE_LIST.split('\n\n')
maps = []
for l in parts:
    first, rest = l.split(':')
    if 'seeds' in first:
        seed_list = rest.split()
    else:
        map_type = first.split()[0]
        maps += [Mapping(map_type,x[0],x[1],x[2]) for x in [y.split() for y in rest.strip().split('\n')]]

print(maps)