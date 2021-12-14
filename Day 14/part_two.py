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


def get_stats(template, original_template):
    stats = dict()

    # count only the first character of each pair,
    # otherwise they get counted twice
    for pair in template:
        if pair[0] not in stats:
            stats[pair[0]] = template[pair]
        else:
            stats[pair[0]] += template[pair]

    # remember to count the last character
    stats[original_template[-1]] += 1

    return stats


def polymerize(template, pairs):
    result = dict()
    
    for pair in template:
        first_pair = pair[0] + pairs[pair]
        second_pair = pairs[pair] + pair[1]
        
        if first_pair not in result:
            result[first_pair] = template[pair]
        else:
            result[first_pair] += template[pair]

        if second_pair not in result:
            result[second_pair] = template[pair]
        else:
            result[second_pair] += template[pair]

    return result


def build_template_dict(template):
    result = dict()

    for i in range(len(template) - 1):
        pair = template[i] + template[i + 1]
        if pair not in result:
            result[pair] = 1
        else:
            result[pair] += 1

    return result


def build_pairs_dict(pairs):
    result = dict()

    for pair_in, pair_out in pairs:
        result[pair_in] = pair_out

    return result


if __name__ == '__main__':
    with open(input_path) as input_data:
        template, pairs = input_data.read().split('\n\n')
        template_dict = build_template_dict(template)
        pairs = build_pairs_dict([pair.split(' -> ') for pair in pairs.split('\n')])

    for step in range(40):
        template_dict = polymerize(template_dict, pairs)

    stats = get_stats(template_dict, template)
    extremes = get_extremes(stats)

    print(stats[extremes['max']] - stats[extremes['min']])
