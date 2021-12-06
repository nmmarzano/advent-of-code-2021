input_path = 'input.txt'


def pass_day(ages):
    return [ages[1], ages[2], ages[3], ages[4], ages[5], ages[6], ages[7] + ages[0], ages[8], ages[0]]


if __name__ == '__main__':
    fishes = []
    ages = [0 for x in range(9)]
    with open(input_path) as input_data:
        fishes = [int(x) for x in input_data.read().split(',')]

    for fish in fishes:
        ages[fish] += 1

    for day in range(256):
        ages = pass_day(ages)

    print(sum(ages))
