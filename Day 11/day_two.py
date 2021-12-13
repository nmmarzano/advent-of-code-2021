input_path = 'input.txt'

dxdy = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def flash_and_count(grid):
    count = 0
    to_flash = []
    flashed = []

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid[y][x] += 1
            if grid[y][x] > 9:
                to_flash.append((x, y))

    while len(to_flash) > 0:
        point = to_flash.pop()
        flashed.append(point)
        for dx, dy in dxdy:
            x, y = point[0] + dx, point[1] + dy
            if x in range(len(grid[0])) and y in range(len(grid)):
                grid[y][x] += 1
                if grid[y][x] > 9 and (x, y) not in to_flash and (x, y) not in flashed:
                    to_flash.append((x, y))
    
    for x, y in flashed:
        grid[y][x] = 0
        count += 1

    return count


if __name__ == '__main__':
    with open(input_path) as input_data:
        grid = [[int(char) for char in line] for line in [line for line in input_data.read().split('\n')]]

    step = 1
    while not flash_and_count(grid) == len(grid) * len(grid[0]):
        step += 1

    print(step)
