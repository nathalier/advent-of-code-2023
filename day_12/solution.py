def parse_p1(data):
    hot_springs, groups = [], []
    for line in data:
        springs, gr = line.split()
        hot_springs.append(springs)
        groups.append(list(map(int, gr.split(','))))
    return hot_springs, groups


def parse_p2(data):
    hot_springs, groups = [], []
    for line in data:
        springs, gr = line.split()
        springs = ((springs + '?') * 5)[:-1]
        gr = ((gr + ',') * 5)[:-1]
        hot_springs.append(springs)
        groups.append(list(map(int, gr.split(','))))
    return hot_springs, groups


def solution(hot_springs, groups):
    res = []
    for s_row, gr in zip(hot_springs, groups):
        res.append(match(tuple(s_row), tuple(gr), cache = {})[0])
        # print(f'{s_row = }, {gr = }; {res[-1] = }')
        # print()
    print(res)
    return sum(res)

def match(s_row, gr, cache):
    # print (f'Matching {s_row} and {gr}')

    if (s_row, gr) in cache:
        # print('returning cached value: ', cache[(s_row, gr)])
        return cache[(s_row, gr)], cache

    if len(s_row) == 0 and len(gr) > 0 or\
       (len(s_row) < sum(gr) + len(gr) - 1) or \
       len(gr) == 0 and '#' in s_row:
        # print('No solution 1, returning 0')
        cache[(s_row, gr)] = 0
        return 0, cache
    
    if len(gr) == 0 and '#' not in s_row:
        # print('returning 1: 1')
        return 1, cache

    res = 0

    if s_row[0] == '.':
        part_res, cache =  match(s_row[1:], gr, cache)
        res += part_res
        cache[(s_row, gr)] = res
        return res, cache
    if s_row[0] == '#':
        if all([s_row[k] in ('#', '?') for k in range(gr[0])]) and \
                (len(s_row) == gr[0] or s_row[gr[0]] in ('.', '?')):
            part_res, cache =  match(s_row[gr[0] + 1:], gr[1:], cache)
            res += part_res
            cache[(s_row, gr)] = res
            return res, cache
        else:
            cache[(s_row, gr)] = res
            # print('No solution 2, adding 0 to res')
            return res, cache
    if s_row[0] == '?' and (len(s_row) >= sum(gr) + len(gr) - 1):
        # print(f'? found, {s_row = }, {gr = }')
        if all([s_row[k] in ('#', '?') for k in range(gr[0])]):
            if (len(s_row) == gr[0] or s_row[gr[0]] in ('.', '?')):
                part_res, cache =  match(s_row[gr[0] + 1:], gr[1:], cache)
                res += part_res
        part_res_ad, cache =  match(s_row[1:], gr, cache)
        res += part_res_ad
        cache[(s_row, gr)] = res
        return res, cache
    else:
        # print('No result')
        cache[(s_row, gr)] = res
        return res, cache
    


def part_2(data):
    return ...


def read_data(filename):
    with open(filename) as f:
        data = list(map(lambda x: x.strip(), f.readlines()))
    return data


#############################
test_data = read_data('input_test.txt')

hot_springs_p1, groups_p1 = parse_p1(test_data)
assert (res := solution(hot_springs_p1, groups_p1)) == 21, f'Actual: {res}'

hot_springs_p2, groups_p2 = parse_p2(test_data)
assert (res := solution(hot_springs_p2, groups_p2)) == 525152, f'Actual: {res}'
#############################


data = read_data('input.txt')

hot_springs_p1, groups_p1 = parse_p1(data)
print(f'Part 1 result: {solution(hot_springs_p1, groups_p1)}')

hot_springs_p2, groups_p2 = parse_p2(data)
print(f'Part 2 result: {solution(hot_springs_p2, groups_p2)}')