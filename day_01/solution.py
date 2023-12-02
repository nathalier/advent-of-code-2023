import re 

def part_1(data):
    first_digit = lambda line: re.match('^[^0-9]*([\d]).*', line).group(1)
    last_digit = lambda line: re.match('^.*(\d)[^0-9]*$', line).group(1)

    return sum(map(lambda l: int(first_digit(l) + last_digit(l)), data))


def part_2(data):
    def to_digit(s): 
        tt = {  'one': '1',
                'two': '2', 
                'three': '3',
                'four': '4',
                'five': '5',
                'six': '6',
                'seven': '7',
                'eight': '8',
                'nine': '9'}
        return tt.get(s, s)
    
    sub_pat = 'one|two|three|four|five|six|seven|eight|nine|[0-9]'

    to_digits = lambda line: list(map(to_digit, re.findall(f'(?=({sub_pat}))', line)))
    digit_lines = [to_digits(line) for line in data]
    
    return sum((int(digits[0] + digits[-1]) for digits in digit_lines))


def read_data(filename):
    with open(filename) as f:
        data = list(map(lambda x: x.strip(), f.readlines()))
    return data


#############################
test_data = read_data('input_test.txt')

assert (res := part_1(test_data)) == 142, f'Actual: {res}'

test_data = read_data('input_test_p2.txt')
assert (res := part_2(test_data)) == 281, f'Actual: {res}'
#############################


data = read_data('input.txt')

print(part_1(data))
print(part_2(data))