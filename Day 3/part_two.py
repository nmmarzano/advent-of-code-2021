input_path = 'input.txt'


def find_most_common(report):
    ones = [0] * len(report[0])

    for line in report:
        for index, bit in enumerate(line):
            if bit == '1':
                ones[index] += 1

    return ['1' if x / len(report) >= 0.5 else '0' for x in ones]


def find_rates(report):
    most_common = find_most_common(report)

    oxygen_candidates = report.copy()
    co2_candidates = report.copy()

    oxygen_most_common = most_common
    co2_most_common = most_common
    
    for i in range(len(report[0])):
        if len(oxygen_candidates) > 1:
            oxygen_candidates = list(filter(lambda x: x[i] == oxygen_most_common[i], oxygen_candidates))
            oxygen_most_common = find_most_common(oxygen_candidates)
        if len(co2_candidates) > 1:
            co2_candidates = list(filter(lambda x: not x[i] == co2_most_common[i], co2_candidates))
            co2_most_common = find_most_common(co2_candidates)

    gamma = int(''.join(most_common), 2)
        
    return {
        'gamma': gamma,
        'epsilon': gamma ^ int(''.join(['1'] * len(most_common)), 2),
        'oxygen_generator': int(oxygen_candidates[0], 2),
        'co2_scrubber': int(co2_candidates[0], 2)
    }


if __name__ == '__main__':
    report = []
    
    with open(input_path) as input_data:
        report = input_data.read().split('\n')
        
    rates = find_rates(report)
    print(rates)
    print(rates['oxygen_generator'] * rates['co2_scrubber'])
