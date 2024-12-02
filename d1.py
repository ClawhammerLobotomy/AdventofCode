
with open('d1_input.txt', 'r') as f:
    x = f.read().split()

# x = [3,4,4,3,2,5,1,3,3,9,3,3]

one = x[::2]
two = x[1::2]


def get_dif(list_one, list_two):
    list_one.sort()
    list_two.sort()
    all_nums = list(zip(list_one, list_two))
    return sum([abs(int(x[0])-int(x[1])) for x in all_nums])

def get_sim(list_one, list_two):
    sim = 0
    for x in list_one:
        count = len([i for i in list_two if i == x])
        sim += count * int(x)
    return sim

dif = get_dif(one, two)
print(dif)
sim = get_sim(one, two)
print(sim)