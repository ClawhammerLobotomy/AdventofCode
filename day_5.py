from collections import namedtuple, defaultdict
from itertools import chain
INPUT_FILE = 'd5_input.txt'
INPUT_FILE = 'd5_test_input.txt'

with open(INPUT_FILE, 'r') as f:
    LINE_LIST = f.read()

"""
Each mapping needs a dictionary of from:to pairs in the range
Starting values = list(range(x[1],x[1]+x[2]))
Seed={
98:50, (50 98 2)
99:51, 
50:52, (52 50 48)
...
97:99
}
"""
class Mapping():
    def __init__(self,first,rest):
        self.map_from, to, self.map_to = first.split()[0].split('-')
        self.map_ranges = rest

Mapping = namedtuple('Mapping',['map_from','map_to','source_start','destination_start','range_length'])
parts = LINE_LIST.split('\n\n')
maps = defaultdict(int)
# maps = []
for l in parts:
    first, rest = l.split(':')
    if 'seeds' in first:
        seed_list = rest.split()
    else:
        map_from, to, map_to = first.split()[0].split('-')
        mapping_keys = [y.split() for y in rest.strip().split('\n')]
        from_ranges = list(chain.from_iterable([list(range(int(x[1]),int(x[1])+int(x[2]))) for x in mapping_keys]))
        to_ranges = list(chain.from_iterable([list(range(int(x[0]),int(x[0])+int(x[2]))) for x in mapping_keys]))
        print('x')
        # maps += [Mapping(map_from,map_to,x[0],x[1],x[2]) for x in [y.split() for y in rest.strip().split('\n')]]

print(maps)