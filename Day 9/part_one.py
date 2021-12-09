input_path = 'input.txt'


def risk_level(cave, point):
    return int(cave[point[1]][point[0]]) + 1


def find_lows(cave):
    lows = set()

    for y, line in enumerate(cave):
        for x, position in enumerate(line):
            position = int(position)
            if not position == 9:
                left = 9 if x <= 0 else int(cave[y][x - 1])
                right = 9 if x >= (len(line) - 1) else int(cave[y][x + 1])
                up = 9 if y <= 0 else int(cave[y - 1][x])
                down = 9 if y >= (len(cave) - 1) else int(cave[y + 1][x])
                if position < left and position < right and position < up and position < down:
                    lows.add((x, y))

    return lows


if __name__ == '__main__':
    with open(input_path) as input_data:
        cave_map = [line for line in input_data.read().split('\n')]

    total_risk = 0
    for low in find_lows(cave_map):
        total_risk += risk_level(cave_map, low)

    print(total_risk)
