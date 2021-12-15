from functools import reduce

input_path = 'input.txt'

dxdy = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def print_grid(grid):
    for line in grid:
        screen_line = ''
        for num in line:
            if num < 10:
                screen_line += '0'
            screen_line += f'{num} '
        print(screen_line)


def find_lowest_risk(grid):
    risk = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]

    to_check = [[0, 0]]
    to_add = []

    while len(to_check) > 0:
        min_distance = reduce(lambda a, b: a if risk[a[1]][a[0]] < risk[b[1]][b[0]] else b, to_check)
        to_check.remove(min_distance)
        x, y = min_distance
        grid[y][x] = 'x'
        to_add = []
        for dx, dy in dxdy:
            if x + dx in range(len(grid[y])) and y + dy in range(len(grid)) and not grid[y + dy][x + dx] == 'x':
                new_risk = risk[y][x] + grid[y + dy][x + dx]
                if risk[y + dy][x + dx] == 0 or risk[y + dy][x + dx] > new_risk:
                    risk[y + dy][x + dx] = new_risk
                if [x + dx, y + dy] not in to_check:
                    to_check.append([x + dx, y + dy])
            
    return risk
    


if __name__ == '__main__':
    with open(input_path) as input_data:
        grid = [[int(num) for num in line] for line in input_data.read().split('\n')]

    risk_grid = find_lowest_risk(grid)

    # print_grid(risk_grid)

    print(risk_grid[len(grid) - 1][len(grid[0]) - 1])
