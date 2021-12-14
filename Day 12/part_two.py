input_path = 'input.txt'


def was_small_cave_already_visited_twice(path):
    small_caves = [cave for cave in path.split('-') if not cave.isupper() and not cave == 'start' and not cave == 'end']
    return not len(small_caves) == len(set(small_caves))


def get_all_paths(paths, travelled):
    full_paths = set()
    new_paths = set()

    for path in paths[travelled.split('-')[-1]]:
        full_path = f'{travelled}-{path}'
        if path == 'start':
            continue
        
        if path == 'end':
            full_paths.add(full_path)
            
        elif path.isupper():
            further_paths = set()
            if not full_path.split('-')[-1] == 'end':
                further_paths = get_all_paths(paths, full_path)
                for further_path in further_paths:
                    if further_path.split('-')[-1] == 'end' and further_path not in full_paths:
                        new_paths.add(further_path)

        else:
            count = len([cave for cave in travelled.split('-') if cave == path])
            if count == 0 or (count == 1 and not was_small_cave_already_visited_twice(travelled)):
                further_paths = set()
                if not full_path.split('-')[-1] == 'end':
                    further_paths = get_all_paths(paths, full_path)
                    for further_path in further_paths:
                        if further_path.split('-')[-1] == 'end' and further_path not in full_paths:
                            new_paths.add(further_path)
                        
    return full_paths.union(new_paths)


def build_paths(links):
    paths = dict()

    for start, end in links:
        if start not in paths:
            paths[start] = [end]
        else:
            paths[start] += [end]
        if end not in paths:
            paths[end] = [start]
        else:
            paths[end] += [start]

    return paths


if __name__ == '__main__':
    links = []
    with open(input_path) as input_data:
        links = [line.split('-') for line in [line for line in input_data.read().split('\n')]]

    paths = build_paths(links)

    full_paths = get_all_paths(paths, 'start')

    print(len(full_paths))
