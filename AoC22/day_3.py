from collections import defaultdict
from string import ascii_lowercase,ascii_uppercase
INPUT_FILE = 'd3_input.txt'
# INPUT_FILE = 'd3_test_input.txt'

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

with open(INPUT_FILE) as f:
    LINE_LIST = f.read().split()

C = defaultdict(int)
for i,x in enumerate(ascii_lowercase+ascii_uppercase):
    C[x] = i+1

priority = 0
for l in LINE_LIST:
    mid = len(l)//2
    first = list(l[:mid])
    second = list(l[mid:])
    priority += [C[x] for x in set(first) & set(second)][0]
print(f"Part 1: {priority}") # 8072

elf_groups = list(chunks(LINE_LIST,3))
priority = 0
for g in elf_groups:
    priority += [C[x] for x in set(g[0]) & set(g[1]) & set(g[2])][0]

print(f"Part 2: {priority}") # 2567