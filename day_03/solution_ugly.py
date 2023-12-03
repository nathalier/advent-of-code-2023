from collections import defaultdict
from operator import mul


def part_1(data):
    numbers, _ = parse_matrix(data)
    engine_parts = []
    m_size = (len(data), len(data[0]))
    
    for i in numbers:
        for j_0, j_1 in numbers[i]:
            ei_0, ei_1, ej_0, ej_1 = get_embed_w_ind(m_size, i, j_0, j_1)
            embed_w_chars = [data[i][j] for i in range(ei_0, ei_1 + 1) for j in range(ej_0, ej_1 + 1)]
            if contains_symb(embed_w_chars):
                engine_parts.append(int(data[i][j_0:j_1+1]))              

    return sum(engine_parts)


def part_2(data):
    numbers, stars = parse_matrix(data)
    m_size = (len(data), len(data[0]))
    gear_ratio = 0

    for i, j in stars:
        ei_0, ei_1, ej_0, ej_1 = get_embed_w_ind(m_size, i, j, j)
        joined_num_pos = joins_numbers_pos(data, ei_0, ei_1, ej_0, ej_1)
        if len(joined_num_pos) > 1:
            joined_numbers = find_numbers(data, numbers, joined_num_pos)
            gear_ratio += mul(*joined_numbers)

    return gear_ratio


def parse_matrix(data):
    numbers = defaultdict(list)
    stars = []

    num_start_j = -1
    for i, row in enumerate(data):
        if num_start_j >= 0:
            numbers[i-1].append((num_start_j, len(data[0]) - 1))
            num_start_j = -1
        for j, c in enumerate(row):
            if c.isdigit():
                if num_start_j < 0:
                    num_start_j = j
            else:
                if num_start_j >= 0:
                    numbers[i].append((num_start_j, j-1))
                    num_start_j = -1
            if c == '*':
                stars.append((i,j))
    
    return numbers, stars


def is_symb(c):
    return not (c.isdigit() or c == '.')

def contains_symb(embed_w_chars):
    return any([is_symb(c) for c in embed_w_chars])


def get_embed_w_ind(m_size, i, j_0, j_1):
    i_0, i_1 = max(0, i-1), min(i+1, m_size[0] - 1)
    j_0, j_1 = max(0, j_0-1), min(j_1+1, m_size[1] - 1)
    return i_0, i_1, j_0, j_1


def joins_numbers_pos(data, ei_0, ei_1, ej_0, ej_1):
    embed_w = [data[i][ej_0: ej_1 + 1] for i in range(ei_0, ei_1 + 1)]
    unique_numbers_pos = []
    
    for i, row in enumerate(embed_w):
        appended = False
        for j, c in enumerate(row):
            if c.isdigit(): 
                if not appended:
                    unique_numbers_pos.append((ei_0 + i, ej_0 + j))
                    appended = True
            else:
                appended = False

    return unique_numbers_pos


def find_numbers(data, numbers, num_pos):
    joined_numbers = []

    for i, j in num_pos: 
        num = int(next(data[i][j_0:j_1+1] for j_0, j_1 in numbers[i] if j_0 <= j <= j_1))
        joined_numbers.append(num)
    return joined_numbers


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