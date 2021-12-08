input_path = 'input.txt'


def count_unique_digits(digits):
    count = 0
    for digit in digits:
        if len(digit) in [2, 4, 3, 7]:
            count += 1
    return count
            


if __name__ == '__main__':
    with open(input_path) as input_data:
        outputs = [line.split(' | ')[1].split() for line in input_data.read().split('\n')]

    digits = []
    for output in outputs:
        digits += output
        
    print(count_unique_digits(digits))
