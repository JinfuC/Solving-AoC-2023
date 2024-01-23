
def extrapolate(part_two=False):

    with open('input.txt') as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        values = [int(value.strip()) for value in line.split(' ')]

        if part_two:
            values = values[::-1]
        
        total+= find_extrapolate(values)
    
    if part_two:
        print('The total sum of the extrapolated values part two is:', total)
    else:
        print('The total sum of the extrapolated values part one is:', total)
    return total

            

def find_extrapolate(current_series:list):

    last_values_series = []

    while len(set(current_series)) != 1:
        last_values_series.append(current_series[-1])
        current_series = [current_series[i+1] - current_series[i] for i in range(0,len(current_series)-1)]
        
    
    last_values_series[-1] += current_series[0]
    
    for i in range(len(last_values_series)-2,-1,-1):
        last_values_series[i] += last_values_series[i+1]

    return last_values_series[0]
        
extrapolate()
extrapolate(True)

                    
