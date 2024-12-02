from collections import namedtuple, defaultdict, deque
from itertools import chain
INPUT_FILE = 'd5_input.txt'
INPUT_FILE = 'd5_test_input.txt'

with open(INPUT_FILE, 'r') as f:
    LINE_LIST = f.read()

"""
Each mapping needs a dictionary of from:to pairs in the range
Starting values = list(range(x[1],x[1]+x[2]))
Mapping values = list(range(int(x[0]),int(x[0])+int(x[2]))
Need a default dictionary with matching key:value pairs for the range of the lowest and highest seeds
Seed={
98:50, (50 98 2)
99:51, 
50:52, (52 50 48)
...
97:99
}
"""


# Mapping = namedtuple('Mapping',['map_from','map_to','source_start','destination_start','range_length'])
parts = LINE_LIST.split('\n\n')

almanac = defaultdict(list)
almanac_key = defaultdict(str)
# maps = []
for l in parts:
    first, rest = l.split(':')
    if 'seeds' in first:
        seed_list = rest.split()
        seed_list_2 = [(int(x),int(y)) for x,y in zip(seed_list[0::2],seed_list[1::2])]
        # dict_range_start = int(min(seed_list))
        # dict_range_end = int(max(seed_list))
    else:
        # maps = defaultdict(int)
        map_from, to, map_to = first.split()[0].split('-')
        almanac_key[map_from] = map_to
        mapping_keys = [y.split() for y in rest.strip().split('\n')]
        range_values = [(int(x[0]),int(x[1]),int(x[2])) for x in mapping_keys]
        # This worked in the test data, but creating a bunch of huge dictionaries into memory crashed my laptop
        # from_ranges = list(chain.from_iterable([list(range(int(x[1]),int(x[1])+int(x[2]))) for x in mapping_keys]))
        # to_ranges = [(int(x[0]),int(x[0])+int(x[2])) for x in mapping_keys]
        # to_ranges = list(chain.from_iterable([list(range(int(x[0]),int(x[0])+int(x[2]))) for x in mapping_keys]))
        # maps = {x:x for x in range(dict_range_start,dict_range_end+1)}
        # for x in range(dict_range_start,dict_range_end+1):
        #     maps[x]=x
        # maps.update({x: y for x,y in zip(from_ranges, to_ranges)})
        almanac[map_to] = range_values
        # dict_range_start = min(maps.values())
        # dict_range_end = max(maps.values())

def find_location(seed):
    current_almanac = 'seed'
    current_index = int(seed)
    while current_almanac != 'location':
        lookup_almanac = almanac_key[current_almanac]
        for keys in almanac[lookup_almanac]:
            if current_index in range(keys[1],keys[1]+keys[2]):
                current_index += keys[0]-keys[1]
                break
        # current_index = almanac[lookup_almanac][current_index]
        current_almanac = lookup_almanac
    # print(f'Seed: {seed} - {lookup_almanac} : {current_index}')
    return current_index

def find_lowest(seed_pair):
    seed_start, seed_range = seed_pair.pop()
    seed_end = seed_start+seed_range
    current_almanac = 'seed'
    while current_almanac != 'location':
        lookup_almanac = almanac_key[current_almanac]
        next_start = 0
        next_end = 0
        for keys in almanac[lookup_almanac]:
            next_start += keys[0]-keys[1]
            next_end += keys[0]-keys[1]
            if current_index in range(keys[1],keys[1]+keys[2]):
                current_index += keys[0]-keys[1]


location_list = []

for sr in seed_list_2:
    location_list.append(find_lowest([sr]))

# for s,r in seed_list_2:
#     print(s,r)
#     location_list.append(map(find_location,range(int(s),int(s)+int(r)))) # Fastest
# print(location_list)
lowest_location = min([find_location(seed) for seed in seed_list])
# lowest_location_2 = min([min(x) for x in location_list])
print(f'Lowest Location 1: {lowest_location}')
# print(f'Lowest Location 2: {lowest_location_2}')
