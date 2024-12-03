import re

with open('d3_input.txt', 'r') as f:
    x = f.read()

# x = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
# x = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
MUL_PAT = re.compile(r'mul\(\d{1,3},\d{1,3}\)')


def extract_mul(mulstring):
    return re.findall(MUL_PAT, mulstring)

def mul(m):
    m = m.replace('mul(', '').replace(')', '').split(',')
    return int(m[0]) * int(m[1])

mul_sum = sum([mul(m) for m in extract_mul(x)])
print(mul_sum)


do_start = x.split('do()')
do_sum = 0
for d in do_start:
    do = d.split("don't()")
    do_sum += sum([mul(m) for m in extract_mul(do[0])])
print(do_sum)