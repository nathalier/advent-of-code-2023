from itertools import starmap
from math import dist
from operator import mul


def parse_p_1(line):
    direction, num, _ = line.split()
    direction, num = direction, int(num)
    return direction, num

def parse_p_2(line):
    _, _, hex = line.split()

    num = int(hex[2:7], 16)
    match hex[7]:
        case '0': direction = 'R'
        case '1': direction = 'D'
        case '2': direction = 'L'
        case '3': direction = 'U'

    return direction, num


def get_area(data, part):
    cur_pos = (0, 0)
    coordinates = [cur_pos]
    for line in data:
        direction, num = parse_p_1(line) if part == 1 else parse_p_2(line)
    
        match direction:
            case 'R': 
                cur_pos = cur_pos[0], cur_pos[1] + num
                coordinates.append((cur_pos[0], cur_pos[1]))
            case 'L': 
                cur_pos = cur_pos[0], cur_pos[1] - num
                coordinates.append((cur_pos[0], cur_pos[1]))
            case 'D': 
                cur_pos = cur_pos[0] + num, cur_pos[1]
                coordinates.append((cur_pos[0], cur_pos[1]))
            case 'U': 
                cur_pos = cur_pos[0] - num, cur_pos[1]
                coordinates.append((cur_pos[0], cur_pos[1]))

    perimeter = sum(map(lambda a: dist(a[0], a[1]), zip(coordinates, coordinates[1:])))

    xs, ys = [p[0] for p in coordinates], [p[1] for p in coordinates]

    half_inner_area = abs(sum(starmap(mul,zip(xs[:-1], ys[1:]))) - 
                          sum(starmap(mul,zip(xs[1:], ys[:-1])))) / 2
    area = half_inner_area + perimeter / 2 + 1
    
    return int(area)


def part_2(data):
    return ...


def read_data(filename):
    with open(filename) as f:
        data = list(map(lambda x: x.strip(), f.readlines()))
    return data


#############################
test_data = read_data('input_test.txt')

assert (res := get_area(test_data, 1)) == 62, f'Actual: {res}'
assert (res := get_area(test_data, 2)) == 952408144115, f'Actual: {res}'
#############################


data = read_data('input.txt')

print(f'Part 1 result: {get_area(data, 1)}')
print(f'Part 2 result: {get_area(data, 2)}')