from functools import reduce

input_path = 'input.txt'

dxdy = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def find_min(points, risk):
    min_point = points[0]
    min_risk = risk[points[0][1]][points[0][0]]

    for point in points:
        if risk[point[1]][point[0]] < min_risk:
            min_point = point
            min_risk = risk[point[1]][point[0]]

    return min_point


def find_lowest_risk(grid):
    risk = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]

    to_check = [[0, 0]]
    to_add = []

    while len(to_check) > 0:
        min_distance = find_min(to_check, risk)
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


def embiggen_grid(grid):
    big_grid = []
    
    for times_i in range(5):
        for i in range(len(grid)):
            new_line = []
            for times_j in range(5):
                for j in range(len(grid[i])):
                    new_line.append(((grid[i][j] + times_i + times_j - 1) % 9) + 1)
            big_grid.append(new_line)

    return big_grid


if __name__ == '__main__':
    with open(input_path) as input_data:
        grid = [[int(num) for num in line] for line in input_data.read().split('\n')]

    grid = embiggen_grid(grid)

    risk_grid = find_lowest_risk(grid)

    print(risk_grid[len(grid) - 1][len(grid[0]) - 1])
