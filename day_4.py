import re
import math
from itertools import count

CARD_NO_PATTERN = r'\d+'
INPUT_FILE = 'd4_test_input.txt'
INPUT_FILE = 'd4_input.txt'

with open(INPUT_FILE, 'r') as f:
    LINE_LIST = f.readlines()


class Card(object):
    _ids = count(1)
    def __init__(self, line, **kwargs):
        self.id = next(self._ids)
        # print(self.id)
        self.line = line
        self.line_list = LINE_LIST
        sections = line.split(':')
        numbers = sections[1].split('|')
        self.card_no = int(re.search(CARD_NO_PATTERN,sections[0]).group(0))
        self.winning_nos = [x for x in numbers[0].strip().split(' ') if x != '']
        self.play_nos = [x for x in numbers[1].strip().split(' ') if x != '']
        self.matching_nos = [x for x in self.play_nos if x in self.winning_nos]
        self.matching_count = len(self.matching_nos)
        self.score = math.pow(2,self.matching_count-1)
        self.winner = any(self.matching_nos)
        self.__dict__.update(kwargs)
        # self.card_copies = [Card(x) for i, x in enumerate(LINE_LIST) if self.card_no < i+1 <= self.card_no+self.matching_count]
        self.card_copies = [Card(x) for x in LINE_LIST[self.card_no:self.card_no+self.matching_count]]


card_classes = [Card(l) for l in LINE_LIST]

total_score = sum([x.score for x in card_classes if x.winner])
total_cards = card_classes[-1].id
print(f'Total Score: {total_score}') # 19135 - Correct
print(f'Total Cards: {total_cards}') # 5704953 - Correct (Took forever to process script)
