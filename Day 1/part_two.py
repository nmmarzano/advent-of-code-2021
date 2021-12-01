input_path = 'input.txt'


def count_increases(measurements):
    count = 0
    for i in range(len(measurements) - 3):
        measurement_one = measurements[i] + measurements[i + 1] + measurements[i + 2]
        measurement_two = measurements[i + 1] + measurements[i + 2] + measurements[i + 3]
        if measurement_one < measurement_two:
            count += 1
    return count
        

if __name__ == '__main__':
    measurements = []
    with (open(input_path) as input_data):
        for line in input_data:
            measurements.append(int(line))
    print(count_increases(measurements))
