def get_winning_combos_num(data):
    cards = [(set(combos[0].split()), set(combos[1].split()))
             for combos in map(lambda l: l.split(':')[1].split('|'), data)]
    return [len(combos[0].intersection(combos[1])) for combos in cards]

def part_1(data):
    winning_combos_num = get_winning_combos_num(data)
    return sum(map(lambda wn: 2**(wn - 1),  
               filter(lambda n: n>0, winning_combos_num)))


def part_2(data):
    winning_combos_num = get_winning_combos_num(data)
    winning_combos_copies = [1] * len(winning_combos_num)

    for i, winning_num in enumerate(winning_combos_num):
        for j in range(i+1, i+winning_num+1):
            winning_combos_copies[j] += winning_combos_copies[i]

    return sum(winning_combos_copies)


def read_data(filename):
    with open(filename) as f:
        data = list(map(lambda x: x.strip(), f.readlines()))
    return data


#############################
test_data = read_data('input_test.txt')

assert (res := part_1(test_data)) == 13, f'Actual: {res}'  # 27454
assert (res := part_2(test_data)) == 30, f'Actual: {res}'  # 6857330
#############################


data = read_data('input.txt')

print(f'Part 1 result: {part_1(data)}')
print(f'Part 2 result: {part_2(data)}')
