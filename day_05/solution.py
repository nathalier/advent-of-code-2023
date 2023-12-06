from operator import itemgetter

def parse_data(filename):
    with open(filename) as f:
        seeds = list(map(int, f.readline().strip().split(': ')[1].split()))
        maps, buffer = {}, []
        
        while (l:=f.readline()):
            line = l.strip()
            if not line:
                continue
            if line.endswith('map:'):
                if buffer:
                    maps[map_name] = sorted(buffer, key=itemgetter(0))
                buffer = []
                map_name = f"{line.split()[0].replace('-', '_')}_map"
                continue
            res, val, count = tuple(map(int, line.split()))
            start, stop, operation = val, val+count-1, res-val
            buffer.append((start, stop, operation))
        maps[map_name] = sorted(buffer, key=itemgetter(0))

    lowest_value = min([maps[mapper][0][0] for mapper in maps])
    largest_value = max([maps[mapper][-1][1] for mapper in maps])
    for mapper in maps:
        if maps[mapper][-1][1] < largest_value:
            maps[mapper].append((maps[mapper][-1][1] + 1, largest_value, 0))
        if maps[mapper][0][0] > lowest_value:
            maps[mapper].append((lowest_value, maps[mapper][0][0]- 1, 0))
        maps[mapper] = sorted(maps[mapper], key=itemgetter(0))

    return seeds, maps


def transform(x, mappers):
    for start, stop, diff_val in mappers:
        if start <= x <= stop:
            return x + diff_val
    return x


def calculate(x, maps):
    for mapper in mapping_order:
        x = transform(x, maps[mapper])
    return x


def get_offset(x, mappers):
    for start, stop, diff_val in mappers:
        if start <= x <= stop:
            return diff_val
    return None


def to_interval_starts(rules):
    interval_starts = []
    i = 0
    while i < len(rules):
        interval_starts.append(rules[i][0])
        if i == len(rules) - 1 or rules[i+1][0] > rules[i][1] + 1:
            interval_starts.append(rules[i][1] + 1)
        i += 1
    return interval_starts

def to_intervals(intervals_start, mappers):
    intervals_start = sorted(intervals_start)
    intervals = []
    for i, interval_st in enumerate(intervals_start[:-1]):
        intervals.append((interval_st, intervals_start[i+1]-1, get_offset(interval_st, mappers)))
    return intervals

    
def split_intervals(maps_1, maps_2):
    interval_starts_1 = to_interval_starts(maps_1)
    interval_starts_2 = to_interval_starts(maps_2)

    interval_mapped = []
    for maps_1_int in maps_1:
        start = transform(maps_1_int[0], maps_1)
        end = transform(maps_1_int[1], maps_1)
        rule = start - maps_1_int[0]
        interval_mapped.append((start, end, rule))

    additional_int_start = []
    for start, end, rule in interval_mapped:
        i = 0
        while i < len(interval_starts_2) and start > interval_starts_2[i]:
            i += 1
        j = i
        while j < len(interval_starts_2) and end >= interval_starts_2[j]:
            pot_add_interval = interval_starts_2[j] - rule
            if pot_add_interval not in interval_starts_1:
                additional_int_start.append(pot_add_interval)
            j += 1

    interval_starts_1.extend(additional_int_start)
    interval_starts_1 = sorted(interval_starts_1)
    updated_intervals = [interv for interv in to_intervals(interval_starts_1, maps_1) if interv[2] is not None]
    return updated_intervals


def part_1(filename):
    seeds, maps = parse_data(filename)

    transformed = []
    for seed in seeds:
        x = seed
        for mapper in mapping_order:
            x = transform(x, maps[mapper])
        transformed.append(x)

    return min(transformed)


def part_2(filename):
    seeds_raw, maps = parse_data(filename)

    seeds_intervals = []
    for i in range(len(seeds_raw) // 2):
        seeds_intervals.append((seeds_raw[2 * i], seeds_raw[2 * i] + seeds_raw[2 * i + 1], 0))
    seeds_intervals = sorted(seeds_intervals, key=itemgetter(0))

    updated_intervals = {}
    updated_intervals['humidity_to_location_map'] = maps['humidity_to_location_map']

    for maps_name in list(zip(mapping_order, mapping_order[1:]))[::-1]:
        updated_intervals[maps_name[0]] = \
                split_intervals(
                     maps[maps_name[0]], 
                     updated_intervals[maps_name[1]])

    seeds_intervals_upd = split_intervals(
                     seeds_intervals, 
                     updated_intervals["seed_to_soil_map"])

    transformed = []
    for interval in seeds_intervals_upd:
        transformed.append(calculate(interval[0], updated_intervals))

    return min(transformed)


mapping_order = ['seed_to_soil_map', 'soil_to_fertilizer_map', 'fertilizer_to_water_map','water_to_light_map',
        'light_to_temperature_map','temperature_to_humidity_map', 'humidity_to_location_map'] 


#############################
test_data = 'input_test.txt'

assert (res := part_1(test_data)) == 35, f'Actual: {res}'
assert (res := part_2(test_data)) == 46, f'Actual: {res}'
#############################


data = 'input.txt'

print(f'Part 1 result: {part_1(data)}')
print(f'Part 2 result: {part_2(data)}')