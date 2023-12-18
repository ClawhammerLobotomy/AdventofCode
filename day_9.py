INPUT_FILE = 'd9_input.txt'
# INPUT_FILE = 'd9_test_input.txt'
with open(INPUT_FILE, 'r') as f:
    L = f.read().split('\n')

seq = [list(map(int,x.split())) for x in L]

class Sequence:
    def __init__(self, row):
        self.row = row
        self.tree_lines = [self.row]
        self.dif_calc()
        self.infer()
        self.rev_infer()
    def dif_calc(self):
        while not all(x==0 for x in self.tree_lines[-1]):
            row = self.tree_lines[-1]
            self.tree_lines += [[row[i+1]-x for i,x in enumerate(row) if i<len(row)-1]]
    def infer(self):
        self.rev_tree = list(reversed(self.tree_lines))
        for i, x in enumerate(self.rev_tree):
            if i < len(self.rev_tree)-1:
                self.rev_tree[i+1].append(x[-1]+self.rev_tree[i+1][-1])
    def rev_infer(self):
        for i, x in enumerate(self.rev_tree):
            if i < len(self.rev_tree)-1:
                self.rev_tree[i+1].insert(0,self.rev_tree[i+1][0]-x[0])
t = [Sequence(x) for x in seq]
new_sum = sum([x.rev_tree[-1][-1] for x in t])
rev_sum = sum([x.rev_tree[-1][0] for x in t])

print(f'Inferred sequence sum: {new_sum}') # 1868368343
print(f'Reverse inferred sequence sum: {rev_sum}') # 1022