input_path = 'input.txt'


def get_extremes(stats):
    maximum = 0
    minimum = stats[list(stats.keys())[0]]
    max_stat = ''
    min_stat = ''

    for char in stats:
        if stats[char] > maximum:
            maximum = stats[char]
            max_stat = char
        elif stats[char] < minimum:
            minimum = stats[char]
            min_stat = char

    return {'max': max_stat, 'min': min_stat}


def get_stats(template):
    stats = dict()

    for char in template:
        if char not in stats:
            stats[char] = 1
        else:
            stats[char] += 1

    return stats


def polymerize(template, pairs):
    result = [template[0]]

    for i in range(len(template) - 1):
        result += [pairs[template[i] + template[i + 1]], template[i + 1]]

    return ''.join(result)


def build_pairs_dict(pairs):
    result = dict()

    for pair_in, pair_out in pairs:
        result[pair_in] = pair_out

    return result


if __name__ == '__main__':
    with open(input_path) as input_data:
        template, pairs = input_data.read().split('\n\n')
        pairs = build_pairs_dict([pair.split(' -> ') for pair in pairs.split('\n')])

    for step in range(10):
        template = polymerize(template, pairs)

    stats = get_stats(template)
    extremes = get_extremes(stats)

    print(stats[extremes['max']] - stats[extremes['min']])
