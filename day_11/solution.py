from operator import itemgetter

def solve(data, expansion_coef=2):
    m_size = len(data), len(data[0])
    star_pos = []
    for i, line in enumerate(data):
        star_pos.extend([(i, j) for j, sym in enumerate(line) if sym == '#'])
    expanding_r = [i for i in range(m_size[0]) if i not in map(itemgetter(0), star_pos)]
    expanding_c = [i for i in range(m_size[0]) if i not in map(itemgetter(1), star_pos)]

    distances = [get_dist(star_pos[i], star_pos[j], expanding_c, expanding_r, expansion_coef) 
                 for i in range(len(star_pos)-1) for j in range(i+1, len(star_pos))]
    return sum(distances)


def get_dist(x, y, expanding_c, expanding_r, expansion_coef):
    dist = abs(y[0] - x[0]) + abs(y[1] - x[1])
    dist += sum([expansion_coef - 1 for i in expanding_r if i in range(x[0], y[0], 1 if y[0] >= x[0] else -1)])
    dist += sum([expansion_coef - 1 for j in expanding_c if j in range(x[1], y[1], 1 if y[1] >= x[1] else -1)])
    return dist


def read_data(filename):
    with open(filename) as f:
        data = list(map(lambda x: x.strip(), f.readlines()))
    return data


#############################
test_data = read_data('input_test.txt')

assert (res := solve(test_data)) == 374, f'Actual: {res}'
assert (res := solve(test_data, 10)) == 1030, f'Actual: {res}'
assert (res := solve(test_data, 100)) == 8410, f'Actual: {res}'
#############################


data = read_data('input.txt')

print(f'Part 1 result: {solve(data)}')
print(f'Part 2 result: {solve(data, 1000000)}')