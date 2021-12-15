## Off by 1 on part 1, off by 3 on part 2, what is going on
## This solution assumes no path ever moves upwards or leftwards, which seems to be true

input_path = 'input.txt'


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

    for y in range(len(grid) - 1, -1, -1):
        for x in range(len(grid[y]) - 1, -1, -1):
            if x + 1 < len(grid[y]) and y + 1 < len(grid):
                risk_down = grid[y + 1][x] + risk[y + 1][x]
                risk_right = grid[y][x + 1] + risk[y][x + 1]
                
                if risk_down < risk_right:
                    risk[y][x] = risk_down
                else:
                    risk[y][x] = risk_right
                    
            elif x + 1 < len(grid[y]):
                risk[y][x] = grid[y][x + 1] + risk[y][x + 1]
                
            elif y + 1 < len(grid):
                risk[y][x] = grid[y + 1][x] + risk[y + 1][x]
                
            else:
                risk[y][x] = 0

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

    # print_grid(risk_grid)

    print(risk_grid[0][0])
