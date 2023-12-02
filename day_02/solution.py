from collections import defaultdict
import re


def get_max_cubes(rounds):
    max_nums = defaultdict(int)
    matches = re.findall('(?P<num>\d+) (?P<color>[a-z]*)', rounds)
    for colour in ('green', 'red', 'blue'):
        max_nums[colour] = max([int(outcome[0]) for outcome in matches if outcome[1] == colour])
    return max_nums


def part_1(data):
    limits = {  'red': 12, 
                'green': 13,
                'blue': 14 }
    game_sum = 0
    
    for line in data:
        m = re.match('Game (\d+): (.*)$', line)
        game_num, rounds = int(m.group(1)), m.group(2)

        max_nums = get_max_cubes(rounds)
        if all([max_nums[colour] <= limits[colour] for colour in limits]):
            game_sum += game_num
    
    return game_sum


def part_2(data):    
    game_sum = 0

    for line in data:
        rounds = re.match('Game \d+: (.*)$', line).group(1)

        max_nums = get_max_cubes(rounds)
        power = max_nums['green'] * max_nums['red'] * max_nums['blue']
        game_sum += power

    return game_sum


def read_data(filename):
    with open(filename) as f:
        data = list(map(lambda x: x.strip(), f.readlines()))
    return data


#############################
test_data = read_data('input_test.txt')

assert (res := part_1(test_data)) == 8, f'Actual: {res}'
assert (res := part_2(test_data)) == 2286, f'Actual: {res}'
#############################


data = read_data('input.txt')

print(f'Part 1 result: {part_1(data)}')
print(f'Part 2 result: {part_2(data)}')