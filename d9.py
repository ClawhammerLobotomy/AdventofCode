from itertools import chain
with open('d9_input.txt', 'r') as f:
    x = f.read().strip()
TEST = False
TEST1 = 1928
PART1 = 6291146824486
TEST2 = 2858
PART2 = 6307279963620
if TEST:
    x = "2333133121414131402"

x = list(x)
files = x[::2]
empty = x[1::2]

file_ids = [[str(i)]*int(n) for i, n in enumerate(files)]
flat_file_ids = list(chain.from_iterable(file_ids))
file_space = [int(n) for n in files]
empty_space = [int(n) for n in empty]
empty_space_dots = [["."]*int(n) if int(n)> 0 else [] for n in empty]

def defrag(file_space, empty_space):
    defragged = []
    for _id_, i in enumerate(file_space):
        for n in range(i):
            try:
                flat_file_ids.pop(0)
                defragged.append(_id_)
            except IndexError:
                return defragged
        empty_count = empty_space.pop(0)
        for j in range(empty_count):
            try:
                f = flat_file_ids.pop(-1)
                defragged.append(f)
            except IndexError:
                return defragged
    return defragged

def defrag_2(file_ids, empty_dots):
    file_count = len(file_ids)
    moved = []

    for i,e in enumerate(file_ids[::-1]):
        print(f'Trying to move file {e}')

        for j in range(len(empty_dots)):
            # print(f'Looking for open spot in position {j}')
            if j > file_count-i-1:
                # print(f'{len(file_ids)-i}')
                # print(f'Passed current position of file {e}. Stop search.')
                break
            space_remaining = [x for x in empty_dots[j] if x == '.']
            if len(e) <= len(space_remaining):
                idx = 0
                for q, dot in enumerate(empty_dots[j]):
                    if idx >= len(e):
                        continue
                    if dot != '.':
                        continue
                    empty_dots[j][q] = e[idx]
                    idx += 1
                moved.append(e)
                break
    remaining_files = []
    for f in file_ids:
        if f in moved:
            f = ['.' for _ in f]
        remaining_files.append(f)
    defragged = list(chain.from_iterable(chain.from_iterable(zip(remaining_files,empty_dots))))
    return defragged


def calc_checksum(defragged_list):
    for i, n in enumerate(defragged_list):
        if n == '.':
            continue
        yield i * int(n)

defrag_list = defrag(file_space, empty_space)
checksum = sum(calc_checksum(defrag_list))
if TEST:
    assert checksum == TEST1
print(f"Part 1: {checksum}")
defrag_list = defrag_2(file_ids, empty_space_dots)
checksum = sum(calc_checksum(defrag_list)) # 6307280105216 - too high, off by one in index to stop searching.
if TEST:
    assert checksum == TEST2
print(f"Part 2: {checksum}")