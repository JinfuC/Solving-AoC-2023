from math import sqrt, floor, ceil

def race(part_two=False):
    with open('input.txt') as f:
        lines = f.readlines()
    _, times = lines[0].split(':')
    _, dists = lines[1].split(':')
    times = times.strip().split(' ')
    dists = dists.strip().split(' ')
    times_race= [t if part_two else int(t) for t in times if t != '']
    dists_race = [d if part_two else int(d) for d in dists if d != '']
    
    # part 2
    if part_two:
        allowed_time = ''
        reach_distance = ''
        for i in range(0, len(dists_race)):
            reach_distance += dists_race[i]
            allowed_time += times_race[i]
        times_race = [int(allowed_time)]
        dists_race = [int(reach_distance)]

    possibilities = 1
    for i in range(0,len(times_race)):
        allowed_time = times_race[i]
        record_distance = dists_race[i]
        # t * (allowed_time - t) > reach_distance
        x1, x2 = calculate_roots(-1,allowed_time,-record_distance)
        # since a < 0, x2 will be the larger root of the two
        possibilities *= floor(x2) - ceil(x1)+1
        # possibilities *= len(list(filter(lambda x: x>x1 and x<x2, range(0,allowed_time+1)))) or this for exhaustive
    
    if part_two:
        print('Product of the number of ways to beat the record part two:', possibilities)
    else:
        print('Product of the number of ways to beat the record part one:', possibilities)
    return 

def calculate_roots(a,b,c):
    D = sqrt(b ** 2 - 4*a*c)
    x1 = (-b + D) / (2*a)
    x2 = (-b - D) / (2*a)
    return x1, x2

race()
race(True)