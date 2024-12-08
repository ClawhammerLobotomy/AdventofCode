from itertools import product
from datetime import datetime
# from math import prod

with open('d7_input.txt', 'r') as f:
    x = f.read().strip().split('\n')

TEST = False
TEST1 = 3749
TEST2 = 11387
PART1 = 12553187650171
if TEST:
    x = [
        '190: 10 19',
        '3267: 81 40 27',
        '83: 17 5',
        '156: 15 6',
        '7290: 6 8 6 15',
        '161011: 16 10 13',
        '192: 17 8 14',
        '21037: 9 7 18 13',
        '292: 11 6 16 20'
    ]
x = [f.split(":") for f in x]
x = [(f[0],f[1].strip().split()) for f in x]


def do_math(eq, symbols, numbers):
    # I misread the assignment and thought we needed to combine these first, not in lef/right order. oops
    # numbers = list(numbers)
    # idx = 0
    # for i, symbol in enumerate(symbols):
    #     if symbol == '||':

    #         # idx = min(idx+i, len(numbers)-1)
    #         r = numbers.pop(idx)
    #         numbers[idx] = r + numbers[idx]
    #     else:
    #         idx +=1
    # symbols = [x for x in symbols if x != '||']
    nums = iter(numbers)
    y = int(next(nums))
    
    for symbol in symbols:
        if y > eq:
            return
        try:
            x = y
            y = int(next(nums))
            # print(x, symbol, y)
            if symbol == '*':
                y = x * y
                continue
            elif symbol == "+":
                y = x + y
                continue
            elif symbol == '||':
                y = int(f"{x}{y}")
                continue
        except StopIteration:
            return y
    return y

def find_solution(oper, eq, *p):
    eq = int(eq)
    v = oper * len(p)
    # comb = list(set(combinations_with_replacement(v,len(p)-1)))
    comb = product(oper, repeat= len(p)-1)
    res = None
    used = []
    for i in comb:
        # print(i)
        if i in used:
            continue
        used.append(i)
        prods = do_math(eq, i, p)
        res = prods
        # print(res)
        if eq == res:
            return res
    return 0

start = datetime.now()


part1_success = 0
oper = ['*','+']
bad = []
for i, j in enumerate(x):
    stat = "No solution"
    now = datetime.now()
    result = find_solution(oper, j[0], *j[1])
    if result:
        stat = "Solution found"
        part1_success += result
        print(f'Loop: {i} is solvable.')
        print(f'Loop: {i} result {result} == {j[0]}')
    else:
        bad.append(j)
    now = datetime.now() - now
    print(f"Loop: {i} {stat} after {now}")
end = datetime.now() - start
print(f'Part 1: {part1_success}')
print(f'Finished part 1 in {end}')

part2_success = 0
oper = ['*','+','||']
for i, j in enumerate(bad):
    stat = "No solution"
    now = datetime.now()
    result = find_solution(oper, j[0], *j[1])
    if result:
        stat = "Solution found"
        part2_success += result
        print(f'Loop: {i} is solvable.')
        print(f'Loop: {i} result {result} == {j[0]}')
    now = datetime.now() - now
    print(f"Loop: {i} {stat} after {now}")
end = datetime.now() - start
print(f'Finished all in {end}')

print(f'Part 2: {part2_success}')
total_success = part1_success + part2_success
print(f'Total Success: {total_success}')
print('Done')