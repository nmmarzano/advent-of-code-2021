input_path = 'input.txt'


def are_both_non_diagonal(line1, line2):
    [[x11, y11], [x12, y12]] = line1
    [[x21, y21], [x22, y22]] = line2
    return x11 == x12 and x11 == x21 and x11 == x22 or y11 == y12 and y11 == y21 and y11 == y22


# ended up going with pure math to eliminate errors
def has_intersection(line1, line2):
    if are_both_non_diagonal(line1, line2):
        return has_non_diagonal_intersection(line1, line2)
    
    [[x11, y11], [x12, y12]] = line1
    [[x21, y21], [x22, y22]] = line2

    x11_x21 = x11 - x21
    x11_x12 = x11 - x12
    x21_x22 = x21 - x22

    y11_y21 = y11 - y21
    y11_y12 = y11 - y12
    y21_y22 = y21 - y22

    d = x11_x12 * y21_y22 - y11_y12 * x21_x22

    if d == 0:
        return True # this is wrong but it's better to have more false positives, method explodes on shared slope
    
    t = (x11_x21 * y21_y22 - y11_y21 * x21_x22) / d
    u = (x11_x21 * y11_y12 - y11_y21 * x11_x12) / d

    return t >= 0.0 and t <= 1.0 and u >= 0.0 and u <= 1.0


def has_non_diagonal_intersection(line1, line2):
    [[x11, y11], [x12, y12]] = line1
    [[x21, y21], [x22, y22]] = line2

    return x11 <= x22 and x12 >= x21 and y11 <= y22 and y12 >= y21


def enumerate_points(line):
    [[x1, y1], [x2, y2]] = line

    points = set()
    points.add((x1, y1))
    points.add((x2, y2))

    if x1 == x2:
        for y in range(y1 + 1, y2):
            points.add((x1, y))
    else:
        for x in range(x1 + 1, x2):
            if y1 == y2:
                points.add((x, y1))
            elif y1 < y2:
                y1 += 1
                points.add((x, y1))
            else:
                y1 -= 1
                points.add((x, y1))
            
    return points


# here's the inefficient one; creates a set of all points in both lines and then calculates the intersection
# mathy methods tried exploded when segments coincide on several points
def list_intersections(line1, line2):
    if are_both_non_diagonal(line1, line2):
        return list_non_diagonal_intersections(line1, line2)
    line1_points = enumerate_points(line1)
    line2_points = enumerate_points(line2)
    intersections = line1_points.intersection(line2_points)
    return intersections


def list_non_diagonal_intersections(line1, line2):
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
            [[line1_x1, line1_y1], [line1_x2, line1_y2]] = lines[i]
            [[line2_x1, line2_y1], [line2_x2, line2_y2]] = lines[j]
            if has_intersection(lines[i], lines[j]):
                intersections = intersections.union(list_intersections(lines[i], lines[j]))
    
    return intersections


# reorders the input data so that the left-most, then top-most point always comes first, for easier processing later
def reorder_points(lines):
    lines = lines.copy()
    for i in range(len(lines)):
        if lines[i][0][0] == lines[i][1][0] and lines[i][0][1] > lines[i][1][1]:
            [lines[i][0], lines[i][1]] = [lines[i][1], lines[i][0]]
        if lines[i][0][0] > lines[i][1][0]:
            [lines[i][0], lines[i][1]] = [lines[i][1], lines[i][0]]
    return lines


if __name__ == '__main__':
    lines = []
    with open(input_path) as input_data:
        lines = [[[int(x) for x in start.split(',')], [int(y) for y in end.split(',')]] for [start, end] in [line.split(' -> ') for line in input_data.read().split('\n')]]

    lines = reorder_points(lines)

    print(len(find_all_intersections(lines)))
