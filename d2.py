with open('d2_input.txt', 'r') as f:
    x = f.read().strip().split('\n')

x = [l.split() for l in x]

x = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]

def find_diff(input_list):
    for i, x in enumerate(input_list):
        if i+1 == len(input_list):
            return
        yield int(x) - int(input_list[i+1])


def safety_check(input_list):
    staging_list = [i for i in input_list]
    if any([abs(x) > 3 for x in staging_list]):
        return 0
    if all([x < 0 for x in staging_list]):
        return 1
    if all([x > 0 for x in staging_list]):
        return 1
    return 0

def dampener(input_list):
    staging_list = [i for i in input_list]
    if any([abs(x) > 3 for x in staging_list]) and len([x for x in staging_list if abs(x) > 3]) > 1 :
        return 0
    if all([x < 0 for x in staging_list]) or len([x for x in staging_list if x < 0]) == 1:
        return 1
    if all([x > 0 for x in staging_list]) or len([x for x in staging_list if x > 0]) == 1:
        return 1
    if len([x for x in staging_list if x == 0]) == 1:
        return 1
    return 0

z = list(map(find_diff, x))
y = list(map(safety_check, z))
print(sum(y))