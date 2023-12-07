from collections import namedtuple, defaultdict, deque
from itertools import chain
INPUT_FILE = 'd5_input.txt'
# INPUT_FILE = 'd5_test_input.txt'

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
        seed_list_2 = [(x,y) for x,y in zip(seed_list[0::2],seed_list[1::2])]
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

# def make_interpolater(left_min, left_max, right_min,right_max):
#     leftSpan = left_max - left_min  
#     rightSpan = right_max - right_min  

#     # Compute the scale factor between left and right values 
#     scaleFactor = float(rightSpan) / float(leftSpan) 

#     # create interpolation function using pre-calculated scaleFactor
#     def interp_fn(value):
#         return right_min + (value-left_min)*scaleFactor

#     return interp_fn
def insertion_sort(list1):  
    # list1 = list(list1)
    # Outer loop to traverse on len(list1)  
    for i in range(1, len(list1)):  

        a = list1[i]  

        # Move elements of list1[0 to i-1], 
        # which are greater to one position
        # ahead of their current position  
        j = i - 1 
        
        while j >= 0 and a < list1[j]:  
            list1[j + 1] = list1[j]  
            j -= 1 
                
        list1[j + 1] = a  
            
    return list1  
def bubbleSort(arr):
     
    n = count(arr)
 
    # For loop to traverse through all 
    # element in an array
    for i in range(n):
        for j in range(0, n - i - 1):
             
            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found 
            #is greater than the adjacent element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def count(iterable):
    if hasattr(iterable, '__len__'):
            return len(iterable)

    d = deque(enumerate(iterable, 1), maxlen=1)
    return d[0][0] if d else 0
# scaler = make_interpolater()
location_list = []
last_location = 10**100
for s,r in seed_list_2:
    print(s,r)
    # location_list.append(min(map(find_location,range(int(s),int(s)+int(r)))))
    location_list.append(map(find_location,range(int(s),int(s)+int(r)))) # Fastest
    # location_list.append(min([find_location(x) for x in range(int(s),int(s)+int(r))]))
    # for x in range(int(s),int(s)+int(r)):
    #     latest_location = find_location(x)
    #     # print(f'Current location: {latest_location}')
    #     if latest_location < last_location:
    #         print(f'Lowest so far: {latest_location}')
    #         location_list.append(latest_location)
    #         last_location = latest_location
# print(location_list)
# lowest_location = min([find_location(seed) for seed in seed_list])
# lowest_location_2 = min([min(x) for x in location_list])
lowest_location_2 = min([insertion_sort(list(x))[0] for x in location_list])
# print(f'Lowest Location 1: {lowest_location}')
print(f'Lowest Location 2: {lowest_location_2}')
