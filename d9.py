from itertools import chain
with open('d9_input.txt', 'r') as f:
    x = f.read().strip()
TEST = False
TEST1 = 1928
PART1 = 6291146824486
TEST2 = 2858
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
    # defragged = []
    tried = []
    moved = []
    # for i in file_ids:
        # _id_ = file_ids[i]
        # defragged.append(_id_)
    for e in file_ids[::-1]:
        if e in tried:
            continue
        tried.append(e)
        for j in range(len(empty_dots)):
            space_remaining = [x for x in empty_dots[j] if x == '.']
            if len(e) <= len(space_remaining):
                # defragged.append(e)
                idx = 0
                for q, dot in enumerate(empty_dots[j]):
                    if idx >= len(e):
                        continue
                    if dot != '.':
                        continue
                    # dot = e[idx]
                    empty_dots[j][q] = e[idx]
                    idx += 1
                moved.append(e)
                break
    remaining_files = []
    for f in file_ids:
        if f in moved:
            f = ['.' for n in f]
        remaining_files.append(f)
    defragged = list(chain.from_iterable(chain.from_iterable(list(zip(remaining_files,empty_dots)))))
    return defragged


def calc_checksum(defragged_list):
    for i, n in enumerate(defragged_list):
        if n == '.':
            continue
        yield i * int(n)

defrag_list = defrag(file_space, empty_space)
checksum = sum(calc_checksum(defrag_list))
print(f"Part 1: {checksum}")
defrag_list = defrag_2(file_ids, empty_space_dots)
checksum = sum(calc_checksum(defrag_list))
print(f"Part 2: {checksum}")