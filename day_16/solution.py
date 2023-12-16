def beam_path(surface, visited, loc, speed):
    splitted = []
    sf_size = len(surface), len(surface[0])
    while (loc, speed) not in visited:
        visited.add((loc, speed))
        
        next_loc = (loc[0] + speed[0], loc[1] + speed[1])
        if not (0 <= next_loc[0] < sf_size[0] and
                0 <= next_loc[1] < sf_size[1]):
            break

        tile = surface[next_loc[0]][next_loc[1]]
        if tile == "." or\
                tile == '|' and speed[1] == 0 or\
                tile == '-' and speed[0] == 0:
            next_speed = speed
        elif tile == "\\":
            next_speed = speed[1], speed[0]
        elif tile == "/":
            next_speed = -speed[1], -speed[0]
        elif tile == '|' and speed[0] == 0:
            splitted.append((next_loc, (-1, 0)))
            next_speed = 1, 0
        elif tile == '-' and speed[1] == 0:
            splitted.append((next_loc, (0, -1)))
            next_speed = 0, 1
        else:
            raise Exception('PANIC!!!')
        
        loc, speed = next_loc, next_speed

    return visited, splitted


def part_1(data, starting_state=((0, -1), (0, 1))):
    visited = set()
    beams = [starting_state]
    while beams:
        visited, new_beams = beam_path(data, visited, *beams.pop(-1))
        beams.extend(new_beams)
    return len(set([t[0] for t in visited])) - 1 # starting point is not on the surface


def part_2(data):
    res = []

    for i in range(len(data)):
        res.append(part_1(data, ((i, -1), (0, 1))))
        res.append(part_1(data, ((i, len(data[0])), (0, -1))))

    for j in range(len(data[0])):
        res.append(part_1(data, ((-1, j), (1, 0))))
        res.append(part_1(data, ((len(data), j), (-1, 0))))

    return max(res)


def read_data(filename):
    with open(filename) as f:
        data = list(map(lambda x: x.strip(), f.readlines()))
    return data


#############################
test_data = read_data('input_test.txt')

assert (res := part_1(test_data)) == 46, f'Actual: {res}'
assert (res := part_2(test_data)) == 51, f'Actual: {res}'
#############################


data = read_data('input.txt')

print(f'Part 1 result: {part_1(data)}')
print(f'Part 2 result: {part_2(data)}')