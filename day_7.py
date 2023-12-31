from collections import defaultdict, Counter
from itertools import chain

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
        self.type = self.type_set(self.hand)
        self.joker_type = self.type_set(self.joker_hand)


    def joker_rule(self):
        c = Counter(self.hand)
        mc = c.most_common()
        if mc[0][0] == 'J' and mc[0][1] == 5: # Most common is Joker, and hand is all jokers. Still 5 of a kind, but lowest score.
            mc = c.most_common()[0][0]
        else: # use the most common non-joker card for replacement.
            mc = [c[0] for c in c.most_common() if c[0] !='J'][0]
        self.joker_hand = self.hand.replace('J',mc)


    def type_set(self, hand):
        hand = hand
        c = Counter(hand)
        n = len(c)
        p = [x for x in c.values()]
        if n == 1:
            return 7 # Five of a kind
        if n == 2:
            if max(p) == 4:
                return 6 # Four of a kind
            if (set([2,3]) & set(p)) == {2,3}:
                return 5 # Full house
        if n == 3:
            if max(p) == 2:
                return 3 # Two pair
            return 4 # Three of a kind
        if n == 4:
            return 2 # One pair
        return 1 # High card


    def card_rank(self):
        for c in self.hand:
            self.card_rankings += [i for i, x in enumerate(card_rank) if x==c]
            self.joker_card_rankings += [i for i, x in enumerate(joker_card_rank) if x==c]


def hand_ranking(hands,rank):
    return sorted(hands, key=lambda x: getattr(x,rank))


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
    full_ranking.append(hand_ranking(group,'card_rankings'))
full_ranking = list(chain.from_iterable(full_ranking))

for i, f in enumerate(full_ranking):
    f.rank = len(full_ranking)-i
    f.score = f.rank * f.bet

total_winnings = sum(f.score for f in full_ranking)
print(f'Total winnings p1: {total_winnings}') # 250058342


full_ranking = []
for key, group in joker_hand_groups:
    full_ranking.append(hand_ranking(group,'joker_card_rankings'))
full_ranking = list(chain.from_iterable(full_ranking))

for i, f in enumerate(full_ranking):
    f.joker_rank = len(full_ranking)-i
    f.joker_score = f.joker_rank * f.bet

total_winnings = sum(f.joker_score for f in full_ranking)
print(f'Total winnings p2: {total_winnings}') # 250506580
# 251149259 - Too high (Jokers were not being replaced properly if they were the most common card.)
# 251106741 - Too high