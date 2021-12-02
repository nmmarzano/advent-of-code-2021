input_path = 'input.txt'


def calculate_path(directions):
    x = 0
    y = 0
    aim = 0
    
    for direction in directions:
        if direction[0] == 'forward':
            x += direction[1]
            y += aim * direction[1]
        elif direction [0] == 'down':
            aim += direction[1]
        elif direction[0] == 'up':
            aim -= direction[1]
    
    return [x, y]


if __name__ == '__main__':
    directions = []
    
    with open(input_path) as input_data:
        for line in input_data:
            split_data = line.strip().split(' ')
            split_data[1] = int(split_data[1])
            directions.append(split_data)
            
    goal = calculate_path(directions)
    print(goal[0] * goal[1])
