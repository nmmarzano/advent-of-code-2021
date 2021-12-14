input_path = 'input.txt'


def fold(points, instruction):
    new_points = []

    axis, fold_line = instruction

    for point in points:
        x, y = point
        
        if axis == 'y' and y > fold_line:
            new_point = [x, 2 * fold_line - y]
        elif axis == 'x' and x > fold_line:
            new_point = [2 * fold_line - x, y]
        else:
            new_point = point
            
        if new_point not in new_points:
            new_points.append(new_point)
            
    
    return new_points


if __name__ == '__main__':
    with open(input_path) as input_data:
        points, instructions = input_data.read().split('\n\n')

    points = [list(map(int, point.split(','))) for point in [point for point in points.split('\n')]]
    instructions = [[instruction.split('=')[0], int(instruction.split('=')[1])] for instruction in [full_instruction.split()[2] for full_instruction in instructions.split('\n')]]

    points = fold(points, instructions[0])

    print(len(points))
