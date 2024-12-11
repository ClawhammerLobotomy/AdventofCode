import math
from itertools import chain
with open('d11_input.txt', 'r') as f:
    x = f.read().strip()
TEST = True
TEST1 = 55312
PART1 = 203609
TEST2 = None
PART2 = None
if TEST:
    x = "125 17"
stones = [int(j) for j in x.split()]


def blink(stones):
    for stone in stones:
        if stone != 0:
            l = int(math.log10(stone)) + 1
        if stone == 0:
            yield [1]
        elif l % 2 == 0:
            mid = int(l/2)
            yield [int(str(stone)[:mid]),int(str(stone)[mid:])]
        else:
            yield [stone * 2024]
def blink_2(stones):
    n = []
    for stone in stones:
        if stone == 0:
            n.append(1)
        else:
            l = int(math.log10(stone)) + 1
            if l % 2 == 0:
                mid = int(l/2)
                n.extend([int(str(stone)[:mid]),int(str(stone)[mid:])])
            else:
                n.append(stone * 2024)
    return n
for _ in range(25):
    stones = chain.from_iterable(blink(stones))
print(f"Part 1: {len(list(stones))}")

stones = [int(j) for j in x.split()]
for i in range(75):
    print(i)
    stones = blink_2(stones)
print(f'Part 2: {len(stones)}')