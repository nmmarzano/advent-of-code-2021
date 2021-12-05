input_path = 'input.txt'


# ended up going with pure math to eliminate errors
def has_intersection(line1, line2):
    [[line1_x1, line1_y1], [line1_x2, line1_y2]] = line1
    [[line2_x1, line2_y1], [line2_x2, line2_y2]] = line2

    x11_x21 = line1_x1 - line2_x1
    x11_x12 = line1_x1 - line1_x2
    x21_x22 = line2_x1 - line2_x2

    y11_y21 = line1_y1 - line2_y1
    y11_y12 = line1_y1 - line1_y2
    y21_y22 = line2_y1 - line2_y2

    d = x11_x12 * y21_y22 - y11_y12 * x21_x22

    if d == 0:
        return True
    
    t = (x11_x21 * y21_y22 - y11_y21 * x21_x22) / d
    u = (x11_x21 * y11_y12 - y11_y21 * x11_x12) / d

    return t >= 0.0 and t <= 1.0 and u >= 0.0 and u <= 1.0


# clamps the points to enumerate to the general area occupied by both lines at the same time, ~1.25 speedup
def enumerate_points_in_range(line, line_range):
    [[x1, y1], [x2, y2]] = line
    xrange = range(max(x1, line_range[0][0]), min(x2, line_range[1][0]) + 1)
    yrange = range(max(y1, line_range[0][1]), min(y2, line_range[1][1]) + 1)

    points = set()

    if x1 == x2:
        for y in yrange:
            points.add((x1, y))

    if y1 == y2:
        for x in xrange:
            points.add((x, y1))
    
    return points


# here's the inefficient one; creates a set of all points in both lines and then calculates the intersection
# mathy methods tried exploded when segments coincide on several points
def list_intersections(line1, line2):
    line1_points = enumerate_points_in_range(line1, line2)
    line2_points = enumerate_points_in_range(line2, line1)
    intersections = line1_points.intersection(line2_points)
    return intersections


# pre-tests if there's an intersection mathematically before trying to list all intersections, almost 2x speedup
def find_all_intersections(lines):
    intersections = set()

    for i in range(len(lines) - 1):
        for j in range(i + 1, len(lines)):
            [[line1_x1, line1_y1], [line1_x2, line1_y2]] = lines[i]
            [[line2_x1, line2_y1], [line2_x2, line2_y2]] = lines[j]
            if has_intersection(lines[i], lines[j]):
                intersections = intersections.union(list_intersections(lines[i], lines[j]))
    
    return intersections


# filter diagonals
def filter_diagonals(lines):
    return [x for x in lines if x[0][0] == x[1][0] or x[0][1] == x[1][1]]


# reorders the input data so that the top-left-most point always comes first, for easier processing later
def reorder_points(lines):
    lines = lines.copy()
    for i in range(len(lines)):
        if lines[i][0][0] == lines[i][1][0] and lines[i][0][1] > lines[i][1][1]:
            [[lines[i][0][0], lines[i][0][1]], [lines[i][1][0], lines[i][1][1]]] = [[lines[i][1][0], lines[i][1][1]], [lines[i][0][0], lines[i][0][1]]]
        if lines[i][0][1] == lines[i][1][1] and lines[i][0][0] > lines[i][1][0]:
            [[lines[i][0][0], lines[i][0][1]], [lines[i][1][0], lines[i][1][1]]] = [[lines[i][1][0], lines[i][1][1]], [lines[i][0][0], lines[i][0][1]]]
    return lines


if __name__ == '__main__':
    lines = []
    with open(input_path) as input_data:
        lines = [[[int(x) for x in start.split(',')], [int(y) for y in end.split(',')]] for [start, end] in [line.split(' -> ') for line in input_data.read().split('\n')]]

    lines = reorder_points(filter_diagonals(lines))

    print(len(find_all_intersections(lines)))
