def parse_data(data):
    tt = {'-': ((0, -1), (0, 1)),
          '|': ((-1, 0), (1, 0)),
          'L': ((-1, 0), (0, 1)),
          'F': ((1, 0), (0, 1)),
          'J': ((-1, 0), (0, -1)),
          '7': ((1, 0), (0, -1)),
          '.': ((0, 0), (0, 0)),
          'S': ((5, 5), (5, 5))}
    pipe_map = []
    for i, line in enumerate(data):
        pipe_map.append([tt[tile] for tile in line])
        if 'S' in line:
            j = line.index('S')
            s_pos = (i, j)
    return pipe_map, s_pos


def get_steps(pipe_map, cell_ind, is_s = False):
    m_size = (len(pipe_map), len(pipe_map[0]))
    if is_s:
        return [(cell_ind[0], cell_ind[1] - b) for b in (-1, 1)  
                    if 0 <= cell_ind[1] - b < m_size[1]] +\
                [(cell_ind[0] - a, cell_ind[1]) for a in (-1, 1)
                    if 0 <= cell_ind[0] - a < m_size[0]] 
    else:
        return [(cell_ind[0] + cell[0], cell_ind[1] + cell[1]) 
                for cell in pipe_map[cell_ind[0]][cell_ind[1]] 
                if 0 <= cell_ind[0] + cell[0] < m_size[0] and\
                   0 <= cell_ind[1] + cell[1] < m_size[1]]


def part_1(data):
    pipe_map, s_pos = parse_data(data)
    path_len = 1
    pos_first_steps = [cell for cell in get_steps(pipe_map, s_pos, is_s = True)]
    next_pos_cell = pos_first_steps.pop(0)
    while s_pos not in get_steps(pipe_map, next_pos_cell):
        # print(f'skipping {next_pos_cell}')
        next_pos_cell = pos_first_steps.pop(0)
    prev_cell, cur_cell = s_pos, next_pos_cell
    path = [s_pos]

    while cur_cell != s_pos:
        path.append(cur_cell)
        next_cell_pos = [cell for cell in get_steps(pipe_map, cur_cell) if cell != prev_cell]
        if not next_cell_pos:
            prev_cell, cur_cell, path_len = s_pos, pos_first_steps.pop(0), 1
            # print('dead end')
        next_cell = next_cell_pos[0]
        if next_cell == s_pos:
            path_len += 1
            break
        next_cell_entries = get_steps(pipe_map, next_cell)
        if cur_cell not in next_cell_entries:
            prev_cell, cur_cell, path_len = s_pos, pos_first_steps.pop(0), 1
            # print('no connection')
        path_len += 1
        prev_cell, cur_cell = cur_cell, next_cell

    return path_len // 2, path


def part_2(data):
    _, path = part_1(data)
    surface = draw_path(data, path)
    enclosed_num = 0
    out = True
    for j in range(len(surface[0])):
        for i in range(len(surface)):
            if surface[i][j] == '.' and not out:
                enclosed_num += 1
                surface[i][j] = 'X'
            elif surface[i][j] in ('J', '7', '-'):
                out = not out

    for row in surface:
        line = ''.join(row)
        print(line)

    return enclosed_num


def draw_path(data, path):
    surface = [['.'] * len(data[0]) for _ in range(len(data))]
    for i, j in path:
        if data[i][j] == 'S':
            match (path[1][0] - path[-1][0], path[1][1] - path[-1][1]):
                case (-1, 1): surface[i][j] = 'F'
                case (0, 2) | (0, -2): 
                    surface[i][j] = '-'
                case (2, 0) | (-2, 0): 
                    surface[i][j] = '|'
                case (1, 1): 
                    surface[i][j] =  '7'
                case (1, -1): 
                    surface[i][j] = 'J'
                case (-1, -1): 
                    surface[i][j] = 'L'
        else:
            surface[i][j] = data[i][j]

    return surface


def read_data(filename):
    with open(filename) as f:
        data = list(map(lambda x: x.strip(), f.readlines()))
    return data


#############################
test_data = read_data('input_test.txt')
test_data_2 = read_data('input_test_2.txt')

assert (res := part_1(test_data)[0]) == 4, f'Actual: {res}'
assert (res := part_1(test_data_2)[0]) == 8, f'Actual: {res}'

test_data_3 = read_data('input_test_3.txt')
assert (res := part_2(test_data_3)) == 4, f'Actual: {res}'
#############################


data = read_data('input.txt')

print(f'Part 1 result: {part_1(data)[0]}')
print(f'Part 2 result: {part_2(data)}')
