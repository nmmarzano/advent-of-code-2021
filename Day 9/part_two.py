input_path = 'input.txt'


def get_surrounding_points(cave, point):
    [x, y] = point
    return {
        'left': (9 if x <= 0 else int(cave[y][x - 1]), (x - 1, y)),
        'right': (9 if x >= (len(cave[0]) - 1) else int(cave[y][x + 1]), (x + 1, y)),
        'up': (9 if y <= 0 else int(cave[y - 1][x]), (x, y - 1)),
        'down': (9 if y >= (len(cave) - 1) else int(cave[y + 1][x]), (x, y + 1))
    }


def basin_size(cave, point):
    basin_points = set()
    to_check = []

    to_check.append(point)

    while len(to_check) > 0:
        cur = to_check.pop()
        basin_points.add(cur)
        points = get_surrounding_points(cave, cur)
        for adjacent in points:
            if not points[adjacent][0] == 9 and not points[adjacent][1] in basin_points and not points[adjacent][1] in to_check:
                to_check.append(points[adjacent][1])

    return len(basin_points)


def find_lows(cave):
    lows = set()

    for y, line in enumerate(cave):
        for x, position in enumerate(line):
            position = int(position)
            if not position == 9:
                points = get_surrounding_points(cave, [x, y])
                if position < points['left'][0] and position < points['right'][0] and position < points['up'][0] and position < points['down'][0]:
                    lows.add((x, y))

    return lows


if __name__ == '__main__':
    with open(input_path) as input_data:
        cave_map = [line for line in input_data.read().split('\n')]

    basin_sizes = []
    for low in find_lows(cave_map):
        basin_sizes.append(basin_size(cave_map, low))

    current_max = 0
    max_total = 1
    for i in range(3):
        current_max = max(*basin_sizes)
        max_total *= current_max
        basin_sizes.remove(current_max)

    print(max_total)
