from collections import Counter
from functools import total_ordering


@total_ordering
class PokerHand:
    def __init__(self, hand, bid, task=1) -> None:
        self.hand = hand
        self.bid = bid
        self.task = task
        self._get_rank()
    
    def _get_rank(self):
        counter = Counter(self.hand)
        cards_in_hand = counter.keys()
        pos_ranks = [self._calculate_rank(self.hand)]
        if self.task == 2 and 'J' in cards_in_hand:
            for c in cards_in_hand:
                if c == 'J':
                    continue
                pos_ranks.append(self._calculate_rank(self.hand.replace('J', c)))
        self.rank = min(pos_ranks)
        

    def _calculate_rank(self, hand):
        counter = Counter(hand)
        if len(counter) == 1:
            return 1
        elif len(counter) == 2 and 4 in counter.values():
            return 2
        elif len(counter) == 2 and sorted(counter.values()) == [2, 3]:
            return 3
        elif 3 in counter.values():
            return 4
        elif len(counter) == 3 and sorted(counter.values()) == [1, 2, 2]:
            return 5
        elif 2 in counter.values():
            return 6
        elif len(counter.values()):
            return 7


    def __eq__(self, other):
        return self.hand == other.hand
    
    def _ordered_str(self, hand):
        tt = {'A': 'E',
              'K': 'D',
              'Q': 'C',
              'J': 'B' if self.task == 1 else '1',
              'T': 'A'}
        return str([tt.get(c, c) for c in hand])
    
    def __gt__(self, other):
        if self.rank == other.rank:
            return self._ordered_str(self.hand) > other._ordered_str(other.hand)
        else: 
            return self.rank < other.rank


def part_1(data, task=1):
    hands = []
    for line in data:
        hand, bid = line.split()
        hands.append(PokerHand(hand, int(bid), task=task))
    hands = sorted(hands)
    score = [(i + 1) * hand.bid for i, hand in enumerate(hands)]
    return sum(score)


def part_2(data):
    print()
    return part_1(data, task=2)


def read_data(filename):
    with open(filename) as f:
        data = list(map(lambda x: x.strip(), f.readlines()))
    return data


#############################
test_data = read_data('input_test.txt')

assert (res := part_1(test_data)) == 6440, f'Actual: {res}'
assert (res := part_2(test_data)) == 5905, f'Actual: {res}'
#############################


data = read_data('input.txt')

print(f'Part 1 result: {part_1(data)}')
print(f'Part 2 result: {part_2(data)}')