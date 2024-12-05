import re

with open('d5_input.txt', 'r') as f:
    x = f.read().strip()

rules = re.findall(r'\d+\|\d+',x)
updates = [u.split(',') for u in x.split() if ',' in u]

TEST = False
if TEST:
    rules = [
        '47|53',
        '97|13',
        '97|61',
        '97|47',
        '75|29',
        '61|13',
        '75|53',
        '29|13',
        '97|29',
        '53|29',
        '61|53',
        '97|53',
        '61|29',
        '47|13',
        '75|47',
        '97|75',
        '47|61',
        '75|61',
        '47|29',
        '75|13',
        '53|13'
        ]
    updates = [ 
        '75,47,61,53,29',
        '97,61,53,29,13',
        '75,29,13',
        '75,97,47,61,53',
        '61,13,29',
        '97,13,75,29,47',
        ]
    updates = [u.split(',') for u in updates]

before = {}
after = {}
for r in rules:
    k, v = r.split('|')
    if k not in before.keys():
        before[k] = []
    before[k].append(v)
    if v not in after.keys():
        after[v] = []
    after[v].append(k)

def order_check(line, reorder=False):
    for i, n in enumerate(line):
        for a in line[i+1::]:
            if n not in before.keys():
                # print(f'No before rule for {n}')
                continue
            if a not in before[n]:
                if not reorder:
                    return False # A number after n is supposed to print before n
                return (i, 'before')
        for a in line[:i:]:
            if a not in after.keys():
                # print(f'No after rule for {a}')
                continue
            if n in after[a]:
                if not reorder:
                    return False # A number before n is supposed to print after n
                return (i, 'after')
    return True

def mid_find(line):
    return int(line[int(len(line)/2)])
def preprocess_constraints(before, after, elements):

    valid_before = {n: set(before.get(n, [])) for n in elements}
    valid_after = {n: set(after.get(n, [])) for n in elements}
    return valid_before, valid_after

def reorder(test_line):
    if order_check(test_line):
        return test_line
    elements = set(test_line)  
    valid_before, valid_after = preprocess_constraints(before, after, elements)
    indices_to_check = set(range(len(test_line)))
    while indices_to_check:
        updated_indices = set()
        for i, n in enumerate(test_line):
            change = False
            pos_offset = 0
            neg_offset = 0

            # Check constraints in `before`
            for j, c in enumerate(test_line[i+1:], start=i+1):
                if c not in valid_before[n]:
                    pos_offset = j + 1
                    change = True
                    break

            # Check constraints in `after`
            for j, c in enumerate(test_line[:i]):
                if c in valid_after[n]:
                    neg_offset = j 
                    change = True
                    break
            
            # Calculate the new position
            new_pos = i + pos_offset + neg_offset
            if new_pos != i and change:
                element = test_line.pop(i)
                test_line.insert(new_pos, element)
                print(f'New position for {n} is {new_pos}')
                updated_indices.update(range(min(i, new_pos), max(i, new_pos) + 1))

        indices_to_check = updated_indices
    return test_line



valid = []
invalid = []
for u in updates:
    if order_check(u):
        valid.append(u)
    else:
        invalid.append(u)
middles = 0
for v in valid:
    middles += mid_find(v)
print(f"Part 1: {middles}")

reorder_check = []
for i in invalid:
    print("="*100)
    print(i)
    x = reorder(i)
    print(f"After: {x}")
    reorder_check.append(x)

middles = 0
for r in reorder_check:
    middles += mid_find(r)

print(f"Part 2: {middles}")