input_path = 'input.txt'


def pass_day(fishes):
    new_fishes = []
    for i in range(len(fishes)):
        if fishes[i] == 0:
            fishes[i] = 6
            new_fishes.append(8)
        else:
            fishes[i] -= 1
    fishes += new_fishes


if __name__ == '__main__':
    fishes = []
    with open(input_path) as input_data:
        fishes = [int(x) for x in input_data.read().split(',')]

    for i in range(80):
        pass_day(fishes)

    print(len(fishes))
