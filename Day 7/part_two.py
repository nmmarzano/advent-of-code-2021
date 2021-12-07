input_path = 'input.txt'


def fuel_cost(crabs, position):
    cost = 0
    for crab in crabs:
        difference = max(crab, position) - min(crab, position)
        for x in range(1, difference + 1):
            cost += x
    return cost


def average(crabs):
    return sum(crabs) / len(crabs)


# first finds the average position as an estimate
# then chooses the direction to check in since there's a single, global minimum
# for example in the real input the average is at 483 and the minimum at 482!
# so we only check a couple positions to find the minimum
# the new weighted fuel cost moves the minimum close to the actual average
def minimum_fuel_cost(crabs):
    crab_average = round(average(crabs))
    cost_at_average = fuel_cost(crabs, crab_average)
    
    if fuel_cost(crabs, crab_average - 1) < cost_at_average:
        position_range = range(crab_average, -1, -1)
    else:
        position_range = range(crab_average, max(crabs))
        
    minimum = cost_at_average
    
    for position in position_range:
        cost = fuel_cost(crabs, position)
        if cost <= minimum:
            minimum = cost
        else:
            break

    return minimum
    

if __name__ == '__main__':
    with open(input_path) as input_data:
        crabs = [int(crab) for crab in input_data.read().split(',')]

    print(minimum_fuel_cost(crabs))
