import re

LIMITS = {
    'blue' : 14,
    'green' : 13,
    'red' : 12
}

class Game:
    def __init__(self, game_results):
        self.game_results = game_results
        parts = game_results.split(':')
        self.id = int(re.search(r'Game (\d+)',parts[0]).group(1))
        self.rounds = [x.strip() for x in parts[1].split(';')]
        self.round_class = [Rounds(r) for r in self.rounds]
        self.invalid = any([x.__dict__ for x in self.round_class if any(y for y in x.__dict__.keys() if LIMITS[y] < x.__getattribute__(y))])
        self.min_red = max(x.red for x in self.round_class)
        self.min_green = max(x.green for x in self.round_class)
        self.min_blue = max(x.blue for x in self.round_class)
        self.power = self.min_red * self.min_green * self.min_blue

class Rounds:
    def __init__(self,results):
        self.red = 0
        self.green = 0
        self.blue = 0
        results = results.split(',')
        r_dic = {re.search(r'[a-zA-Z]+',r).group(0):int(re.search(r'\d+',r).group(0)) for r in results}
        self.__dict__.update(**r_dic)

input_file = 'd2_input.txt'
# input_file = 'd2_test_input.txt'

with open(input_file, 'r') as f:
    lines = f.readlines()
    game_list = [Game(l) for l in lines]
    id_sum = sum([x.id for x in game_list if x.invalid == False])
    power_sum = sum([x.power for x in game_list])
    print(f'ID sum: {id_sum}')
    print(f'Power sum: {power_sum}')