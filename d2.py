with open('d2_input.txt', 'r') as f:
    x = f.read().strip().split('\n')

x = [l.split() for l in x]

# x = [
#     [7, 6, 4, 2, 1],
#     [1, 2, 7, 8, 9],
#     [9, 7, 6, 2, 1],
#     [1, 3, 2, 4, 5],
#     [8, 6, 4, 4, 1],
#     [1, 3, 6, 7, 9]
# ]

def find_diff(input_list):
    return [int(x) - int(input_list[i+1]) for i, x in enumerate(input_list) if i + 1 < len(input_list)]

def safety_check(l):
    diff = find_diff(l)
    if any([abs(x) > 3 for x in diff]):
        return 0
    if all([x < 0 for x in diff]):
        return 1
    if all([x > 0 for x in diff]):
        return 1
    return 0

def dampener(input_list):
    for n in range(len(input_list)):
        new_list = list(input_list)
        new_list.pop(n)
        if safety_check(new_list):
            return 1
    return 0


safe = 0
use_dampener = 1
for l in x:
    if safety_check(l):
        safe += 1
        continue
    if dampener(l) and use_dampener:
        safe += 1
        continue
print(safe)
