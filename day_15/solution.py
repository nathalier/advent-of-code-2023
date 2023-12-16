from collections import defaultdict


def part_1(data):
    return sum(map(get_hash,  data[0].split(',')))


def part_2(data):
    boxes = defaultdict(dict)
    for lense in data[0].split(','):
        if lense[-1] == '-':
            label = lense[:-1]
            hsh = get_hash(label)
            boxes[hsh].pop(label, 0)
        elif lense[-2] == '=':
            label, power = lense.split('=')
            hsh = get_hash(label)
            boxes[hsh][label] = int(power)
    
    return sum([(i + 1) * (j + 1) * power 
                for i, box in boxes.items() 
                for j, power in enumerate(box.values())])


def get_hash(token: str):
    hash_res = 0
    for char in token:
        hash_res = (hash_res + ord(char)) * 17 % 256
    return hash_res


def read_data(filename):
    with open(filename) as f:
        data = list(map(lambda x: x.strip(), f.readlines()))
    return data


#############################
test_data = read_data('input_test.txt')

assert (res := part_1(test_data)) == 1320, f'Actual: {res}'
assert (res := part_2(test_data)) == 145, f'Actual: {res}'
#############################


data = read_data('input.txt')

print(f'Part 1 result: {part_1(data)}')
print(f'Part 2 result: {part_2(data)}')