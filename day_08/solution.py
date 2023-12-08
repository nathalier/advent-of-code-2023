from itertools import cycle
from math import lcm
import re

"""
The solution of p.2 is actually is not completely correct, 
as I'm breaking at the first found 'Z'-position while it's possible that the next 'Z'-position 
for a ghost would give better result. 
I.e. LCM(5, 14) = 70; while it's possible that the first ghost finds 'Z'-position at 7th step as well.
Then LCM(7, 17) = 14. But this simple, technically invalid, solution worked on my entry:-)
"""


def parse_map(data):
    g_map = {} 
    for line in data[2:]:
        place, turns = line.split(' = ')
        lt, rt = re.findall('([0-9A-Z]{3})', turns)
        g_map[place] = (lt, rt)

    turns_pattern = [int(ch) for ch in data[0].replace('L', '0').replace('R', '1')]

    return g_map, turns_pattern


def part_1(data):
    g_map, turns_pattern = parse_map(data)
    turns = cycle(turns_pattern)

    curr, end = 'AAA', 'ZZZ'
    counter = 0
    while curr != end:
        curr = g_map[curr][next(turns)]
        counter += 1

    return counter


def part_2(data):
    g_map, turns_pattern = parse_map(data)

    def get_min_way(curr):
        turns = cycle(turns_pattern)
        counter = 0

        while not curr.endswith('Z'):
            curr = g_map[curr][next(turns)]
            counter += 1

        return counter


    curr_locs = [loc for loc in g_map.keys() if loc.endswith('A')]

    min_ways_length = []
    for loc in curr_locs:
        min_ways_length.append(get_min_way(loc))

    return lcm(*min_ways_length)


def read_data(filename):
    with open(filename) as f:
        data = list(map(lambda x: x.strip(), f.readlines()))
    return data


#############################
test_data = read_data('input_test.txt')
assert (res := part_1(test_data)) == 2, f'Actual: {res}'

test_data_2 = read_data('input_test_2.txt')
assert (res := part_1(test_data_2)) == 6, f'Actual: {res}'

test_data_3 = read_data('input_test_3.txt')
assert (res := part_2(test_data_3)) == 6, f'Actual: {res}'
#############################


data = read_data('input.txt')

print(f'Part 1 result: {part_1(data)}')
print(f'Part 2 result: {part_2(data)}')