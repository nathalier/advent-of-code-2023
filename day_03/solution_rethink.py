from collections import defaultdict
from operator import mul
import re


def part_1(data):
    numbers = parse_matrix(data)
    engine_parts = []
    m_size = (len(data), len(data[0]))
    
    for i, j_0, j_1, num in numbers:
        embed_w = get_embed_w(m_size, i, j_0, j_1)
        if any([is_symb(data[ei][ej]) for ei, ej in embed_w]):
            engine_parts.append(num)              

    return sum(engine_parts)


def part_2(data):
    numbers = parse_matrix(data)
    m_size = (len(data), len(data[0]))

    star_adj_numbers = defaultdict(list)
    gear_ratio = 0

    for i, j_0, j_1, num in numbers:
        embed_w = get_embed_w(m_size, i, j_0, j_1)
        for ei, ej in embed_w:
            if data[ei][ej] == '*':
                star_adj_numbers[ei, ej].append(num)
    
    gear_ratio = sum([
                    mul(*star_adj_numbers[star]) for star in star_adj_numbers
                    if len(star_adj_numbers[star]) > 1])

    return gear_ratio


def parse_matrix(data):
    numbers = []
    for i, line in enumerate(data):
        for m in re.finditer('\d+', line):
            numbers.append((i, m.start(), m.end(), int(m.group(0))))
    return numbers


def is_symb(c):
    return not (c.isdigit() or c == '.')


def get_embed_w(m_size, i, j_0, j_1):
    i_0, i_1 = max(0, i-1), min(i+1, m_size[0] - 1)
    j_0, j_1 = max(0, j_0-1), min(j_1, m_size[1] - 1)
    return [(i, j) for i in range(i_0, i_1 + 1) for j in range(j_0, j_1 + 1)]


def read_data(filename):
    with open(filename) as f:
        data = list(map(lambda x: x.strip(), f.readlines()))
    return data


#############################
test_data = read_data('input_test.txt')

assert (res := part_1(test_data)) == 4361, f'Actual: {res}'
assert (res := part_2(test_data)) == 467835, f'Actual: {res}'
#############################


data = read_data('input.txt')

print(f'Part 1 result: {part_1(data)}')  # Part 1 result: 537732
print(f'Part 2 result: {part_2(data)}')  # Part 2 result: 84883664
