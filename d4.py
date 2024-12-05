import re

def chunk_list(lst:list, chunk_size:int, offset:int=0):
    for i in range(offset, len(lst), chunk_size):
        yield lst[i:i + chunk_size]


with open('d4_input.txt', 'r') as f:
    x = f.read().strip().split()

# x = [
#     'MMMSXXMASM',
#     'MSAMXMSMSA',
#     'AMXSXMAAMM',
#     'MSAMASMSMX',
#     'XMASAMXAMM',
#     'XXAMMXXAMA',
#     'SMSMSASXSS',
#     'SAXAMASAAA',
#     'MAMMMXMMMM',
#     'MXMXAXMASX'
# ]



PAT = r'MAS'
SEARCH = re.compile(PAT)


def xmas_extract(input_string):
    f = len(re.findall(SEARCH, input_string))
    
    r = len(re.findall(SEARCH, input_string[::-1]))
    
    if f + r > 0:
        print(input_string)
        print(f'Forward matches: {f}')
        print(f'Reverse matches: {r}')
    return  f + r

def x_mas_extract(input_tuple):
    x = 0
    for t in input_tuple:
        f = len(re.findall(SEARCH, t))
        r = len(re.findall(SEARCH, t[::-1]))
        if f+r >0:
            x+=1
    return 1 if x == 2 else 0


def array_rotate(input_list):
    new_list = []
    for i in range(len(input_list[0])):
        new_list.append(''.join([x[i] for x in input_list]))
    return new_list


def array_shift(input_list):
    """
    every 4 rows, need to remove increasingly more characters from the start and decreasingly less from the end
    row 0 - 0 from the start, 3 from the end
    row 1 - 1 / 2
    row 2 - 2 / 1
    row 3 - 3 / 0
    """
    new_list = []
    rev = []
    for i, x in enumerate(input_list):
        new_list.append(x[i:len(x)-(len(PAT)-1)+i])
        rev.append(x[(len(PAT)-1)-i:len(x)-i])
    return new_list, rev

def diag_check(input_list):
    word_count = 0
    x_mas_count = 0
    for i in range(len(PAT)):
        sets = list(chunk_list(input_list, len(PAT), i))
        for chunk in sets:
            if len(chunk) < len(PAT):
                continue
            print("="*50)
            print(f"Chunk: {chunk}")
            lshift, rshift = array_shift(chunk)
            lchunk = array_rotate(lshift)
            rchunk = array_rotate(rshift)
            xchunks = list(zip(lchunk,rchunk))
            
            for x in xchunks:
                x_mas_count += x_mas_extract(x)
            c = 0
            print("="*50)
            print(f"Checking Left Chunk: {lchunk}")
            for w in lchunk:
                c += xmas_extract(w)
            print(f'Matches diagonally right: {c}')
            word_count += c
            c = 0
            print("="*50)
            print(f"Checking Right Chunk: {rchunk}")
            for w in rchunk:
                c += xmas_extract(w)
            print(f'Matches diagonally left: {c}')
            word_count += c
    return word_count if PART_1 else x_mas_count

PART_1 = False
words = 0

for l in x:
    words += xmas_extract(l)
rotated_list = array_rotate(x)
for l in rotated_list:
    words += xmas_extract(l)
words += diag_check(x)

x_mas_words = diag_check(x)

print(f"Part 1: {words}")
print(f"Part 2: {x_mas_words}")