from functools import reduce
from math import ceil, floor
from operator import mul


def parse_data(data):
    times = list(map(int, data[0].split(':')[1].strip().split()))
    distances = list(map(int, data[1].split(':')[1].strip().split()))
    return list(zip(times, distances))



def solve_race(race):
    race_time, best_time = race
    total_strat = race_time + 1

    min_time_wait = 1 + int((race_time - (race_time ** 2 - 4 * best_time) ** (1/2))/2)
    loss_strat_count = min_time_wait * 2

    return total_strat - loss_strat_count


def part_1(data):
    races = parse_data(data)

    win_strat_counts = []
    for race in races:
        win_strat_counts.append(solve_race(race))

    return reduce(mul, win_strat_counts, 1)


def part_2(data):
    race = parse_data(list(map(lambda l: l.replace(' ', ''), data)))[0]

    win_strat_count = solve_race(race)
    return win_strat_count


def read_data(filename):
    with open(filename) as f:
        data = list(map(lambda x: x.strip(), f.readlines()))
    return data


#############################
test_data = read_data('input_test.txt')

assert (res := part_1(test_data)) == 288, f'Actual: {res}'  # 1710720
assert (res := part_2(test_data)) == 71503, f'Actual: {res}'  # 35349468
#############################


data = read_data('input.txt')

print(f'Part 1 result: {part_1(data)}')
print(f'Part 2 result: {part_2(data)}')