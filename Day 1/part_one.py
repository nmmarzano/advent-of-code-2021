input_path = 'input.txt'


def count_increases(measurements):
    count = 0
    for i in range(len(measurements) - 1):
        if measurements[i] < measurements[i + 1]:
            count += 1
    return count
        

if __name__ == '__main__':
    measurements = []
    with (open(input_path) as input_data):
        for line in input_data:
            measurements.append(int(line))
    print(count_increases(measurements))
