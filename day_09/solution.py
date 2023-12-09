def part_1(data):
    res = 0 
    for line in data:
        values = [int(v) for v in line.split()]
        last_values = [values[-1]]
        while not all([v == 0 for v in values]):
            values = [j - i for i, j in zip(values, values[1:])]
            last_values.append(values[-1])
        res += sum(last_values)
    return res


def part_2(data):
    res = 0 
    for line in data:
        values = [int(v) for v in line.split()]
        last_values = [values[0]]
        multiplier = -1
        while not all([v == 0 for v in values]):
            values = [j - i for i, j in zip(values, values[1:])]
            last_values.append(multiplier * values[0])
            multiplier *= -1
        res += sum(last_values)
    return res


def read_data(filename):
    with open(filename) as f:
        data = list(map(lambda x: x.strip(), f.readlines()))
    return data


#############################
test_data = read_data('input_test.txt')

assert (res := part_1(test_data)) == 114, f'Actual: {res}'
assert (res := part_2(test_data)) == 2, f'Actual: {res}'
#############################


data = read_data('input.txt')

print(f'Part 1 result: {part_1(data)}')
print(f'Part 2 result: {part_2(data)}')