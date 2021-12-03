input_path = 'input.txt'


def find_rates(report):
    ones = [0] * len(report[0])

    for line in report:
        for index, bit in enumerate(line):
            if bit == '1':
                ones[index] += 1

    most_common = ['1' if x / len(report) >= 0.5 else '0' for x in ones]
    
    gamma = int(''.join(most_common), 2)
    epsilon = gamma ^ int(''.join(['1'] * len(most_common)), 2)
    
    return {'gamma': gamma, 'epsilon': epsilon}


if __name__ == '__main__':
    report = []
    
    with open(input_path) as input_data:
        report = input_data.read().split('\n')
        
    rates = find_rates(report)
    print(rates['gamma'] * rates['epsilon'])
