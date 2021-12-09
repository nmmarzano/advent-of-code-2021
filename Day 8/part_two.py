input_path = 'input.txt'

digits = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
always_on = ['', '', 'cf', 'acf', 'bcdf', 'adg', 'abfg', 'abcdefg']


def decode(substitutions, numbers):
    results = []
    
    for number in numbers:
        result = []
        for char in number:
            result.append(substitutions[char])
        result.sort()
        result = ''.join(result)
        for i, digit in enumerate(digits):
            if result == digit:
                results.append(i)

    return results[0] * 1000 + results[1] * 100 + results[2] * 10 + results[3]


def find_substitutions(digits):
    segments = set(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    
    baskets = {
        'a': segments,
        'b': segments,
        'c': segments,
        'd': segments,
        'e': segments,
        'f': segments,
        'g': segments
    }

    for digit in digits:
        chars = set([char for char in digit])
        for char in always_on[len(digit)]:
            baskets[char] = baskets[char].intersection(chars)

    solved = set()

    while len(solved) < 7:
        for char in baskets:
            if len(baskets[char]) > 1:
                for solved_char in solved:
                    if solved_char in baskets[char]:
                        baskets[char].remove(solved_char)
            if len(baskets[char]) == 1:
                solved.add(*baskets[char])

    substitutions = dict()
    for char in baskets:
        for solution in baskets[char]: # it's always just the one
            substitutions[solution] = char

    return substitutions


def count_unique_digits(digits):
    count = 0
    for digit in digits:
        if len(digit) in [2, 4, 3, 7]:
            count += 1
    return count
            


if __name__ == '__main__':
    with open(input_path) as input_data:
        data = input_data.read().split('\n')
        inputs = [line.split(' | ')[0].split() for line in data]
        outputs = [line.split(' | ')[1].split() for line in data]

    total = 0
    for i in range(len(outputs)):
        substitutions = find_substitutions(inputs[i] + outputs[i])
        total += decode(substitutions, outputs[i])

    print(total)
