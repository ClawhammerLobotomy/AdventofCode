INPUT_FILE = 'd1_input.txt'
# INPUT_FILE = 'd1_test_input.txt'

with open(INPUT_FILE) as f:
    LINE_LIST = f.read()

elf_inv = [sum(int(y) for y in x.split('\n')) for x in LINE_LIST.split('\n\n')]
sort_inv = sorted(elf_inv, reverse=True)
most_cals = max(elf_inv)
top3 = sum(sort_inv[:3])
print(most_cals)
print(top3)