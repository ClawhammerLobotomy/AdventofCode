from collections import namedtuple, defaultdict, deque, Counter
from itertools import chain, groupby
import math
INPUT_FILE = 'd7_input.txt'
# INPUT_FILE = 'd7_test_input.txt'

with open(INPUT_FILE, 'r') as f:
    LINE_LIST = f.read().split('\n')

card_rank = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
joker_card_rank = ['A','K','Q','T','9','8','7','6','5','4','3','2','J']
class CamelHand:
    def __init__(self,row):
        self.hand = row.split()[0]
        self.bet = int(row.split()[1])
        self.card_rankings = []
        self.joker_card_rankings = []
        self.joker_rule()
        self.card_rank()
        self.hand_type()
        self.joker_type()
    
    
    def joker_rule(self):
        c = Counter(self.hand)
        mc = c.most_common()
        if mc[0][0] == 'J' and mc[0][1] == 5: # Most common is Joker, and hand is all jokers. Still 5 of a kind, but lowest score.
            mc = c.most_common()[0][0]
        else: # use the most common non-joker card for replacement.
            mc = [c[0] for c in c.most_common() if c[0] !='J'][0]
        self.joker_hand = self.hand.replace('J',mc)
        

    def joker_type(self):
        hand = self.joker_hand
        c = Counter(hand)
        n = len(c)
        p = [x for x in c.values()]
        if n == 1:
            self.joker_type = 7
            return # Five of a kind
        if n == 2:
            if max(p) == 4:
                self.joker_type = 6
                return # Four of a kind
            if (set([2,3]) & set(p)) == {2,3}:
                self.joker_type = 5
                return # Full house
        if n == 3:
            if max(p) == 2:
                self.joker_type = 3
                return # Two pair
            self.joker_type = 4
            return # Three of a kind
        if n == 4:
            self.joker_type = 2
            return # One pair
        self.joker_type = 1
        return # High card
    

    def hand_type(self):
        hand = self.hand
        c = Counter(hand)
        n = len(c)
        p = [x for x in c.values()]
        if n == 1:
            self.type = 7
            return # Five of a kind
        if n == 2:
            if max(p) == 4:
                self.type = 6
                return # Four of a kind
            if (set([2,3]) & set(p)) == {2,3}:
                self.type = 5
                return # Full house
        if n == 3:
            if max(p) == 2:
                self.type = 3
                return # Two pair
            self.type = 4
            return # Three of a kind
        if n == 4:
            self.type = 2
            return # One pair
        self.type = 1
        return # High card
    

    def card_rank(self):
        for c in self.hand:
            self.card_rankings += [i for i, x in enumerate(card_rank) if x==c]
            self.joker_card_rankings += [i for i, x in enumerate(joker_card_rank) if x==c]


def hand_ranking(hands):
    return sorted(hands, key=lambda x: x.card_rankings)


def groupby_unsorted(seq, key=lambda x: x):
    indexes = defaultdict(list)
    for i, elem in enumerate(seq):
        indexes[key(elem)].append(i)
    for k, idxs in indexes.items():
        yield k, (seq[i] for i in idxs)



hand_types = [CamelHand(h) for h in LINE_LIST]
hand_groups = groupby_unsorted(hand_types, lambda x: x.type)
hand_groups = sorted(hand_groups, key=lambda x:x[0], reverse=True)
joker_hand_groups = groupby_unsorted(hand_types, lambda x: x.joker_type)
joker_hand_groups = sorted(joker_hand_groups, key=lambda x:x[0], reverse=True)


full_ranking = []
for key, group in hand_groups:
    full_ranking.append(hand_ranking(group))
full_ranking = list(chain.from_iterable(full_ranking))

for i, f in enumerate(full_ranking):
    f.rank = len(full_ranking)-i
    f.score = f.rank * f.bet

total_winnings = sum(f.score for f in full_ranking)
print(f'Total winnings p1: {total_winnings}') # 250058342


full_ranking = []
for key, group in joker_hand_groups:
    full_ranking.append(sorted(group, key=lambda x: x.joker_card_rankings))
full_ranking = list(chain.from_iterable(full_ranking))

for i, f in enumerate(full_ranking):
    f.joker_rank = len(full_ranking)-i
    f.joker_score = f.joker_rank * f.bet

total_winnings = sum(f.joker_score for f in full_ranking)
print(f'Total winnings p2: {total_winnings}') # 250506580
# 251149259 - Too high
# 251106741 - Too high