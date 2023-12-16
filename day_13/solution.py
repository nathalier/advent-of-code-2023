import numpy as np


def calculate(mx, smudge_adj=0):
    for i in range(mx.shape[0] - 1):
        if rows_symmetric(mx[i], mx[i + 1]) or\
               rows_symmetric(mx[i], mx[i + 1], smudge_adj):
            rows_num = min(i + 1, mx.shape[0] - i - 1)
            if rows_symmetric(mx[i - rows_num + 1 : i + 1], 
                              np.flip(mx[i + 1 : i + rows_num + 1], 0), smudge_adj):
                return i + 1
    return 0


def rows_symmetric(a, b, smudge_adj=0, tol=1e-8):
    return smudge_adj - tol < np.sum(np.abs(a-b)) < smudge_adj + tol


def part_1(data, smudge_adj=0):
    data.append('')
    res = 0
    surface = []
    for line in data:
        if not line:
            mx = np.array(surface)
            res += 100 * calculate(mx, smudge_adj)
            res += calculate(mx.T, smudge_adj)
            surface = []
        else:
            surface.append([1 if ch == '#' else 0 for ch in line])
    return res


def read_data(filename):
    with open(filename) as f:
        data = list(map(lambda x: x.strip(), f.readlines()))
    return data


#############################
test_data = read_data('input_test.txt')

assert (res := part_1(test_data)) == 405, f'Actual: {res}'
print()
assert (res := part_1(test_data, smudge_adj=1)) == 400, f'Actual: {res}'
#############################


data = read_data('input.txt')

print(f'Part 1 result: {part_1(data)}')
print(f'Part 2 result: {part_1(data, smudge_adj=1)}')