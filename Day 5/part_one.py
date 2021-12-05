input_path = 'input.txt'


# no more maths, massive speedup
def has_intersection(line1, line2):
    [[x11, y11], [x12, y12]] = line1
    [[x21, y21], [x22, y22]] = line2

    return x11 <= x22 and x12 >= x21 and y11 <= y22 and y12 >= y21


def list_intersections(line1, line2):
    [[x11, y11], [x12, y12]] = line1
    [[x21, y21], [x22, y22]] = line2

    points = set()

    if x11 == x12:
        yrange = range(max(y11, y21), min(y12, y22) + 1)
        for y in yrange:
            points.add((x11, y))
    elif y11 == y12:
        xrange = range(max(x11, x21), min(x12, x22) + 1)
        for x in xrange:
            points.add((x, y11))
    return points


# pre-tests if there's an intersection mathematically before trying to list all intersections, almost 2x speedup
def find_all_intersections(lines):
    intersections = set()

    for i in range(len(lines) - 1):
        for j in range(i + 1, len(lines)):
            if has_intersection(lines[i], lines[j]):
                intersections = intersections.union(list_intersections(lines[i], lines[j]))
    
    return intersections


# filter diagonals
def filter_diagonals(lines):
    return [line for line in lines if line[0][0] == line[1][0] or line[0][1] == line[1][1]]


# reorders the input data so that the top-left-most point always comes first, for easier processing later
def reorder_points(lines):
    lines = lines.copy()
    for i in range(len(lines)):
        if lines[i][0][0] == lines[i][1][0] and lines[i][0][1] > lines[i][1][1]:
            [lines[i][0], lines[i][1]] = [lines[i][1], lines[i][0]]
        if lines[i][0][1] == lines[i][1][1] and lines[i][0][0] > lines[i][1][0]:
            [lines[i][0], lines[i][1]] = [lines[i][1], lines[i][0]]
    return lines


if __name__ == '__main__':
    lines = []
    with open(input_path) as input_data:
        lines = [[[int(x) for x in start.split(',')], [int(y) for y in end.split(',')]] for [start, end] in [line.split(' -> ') for line in input_data.read().split('\n')]]

    lines = reorder_points(filter_diagonals(lines))

    print(len(find_all_intersections(lines)))
