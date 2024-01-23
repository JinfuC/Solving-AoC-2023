from ast import literal_eval
from math import lcm

def wasteland(part_two=False):
    
    with open('input.txt') as f:
        lines = f.readlines()

    mapping = {}
    instructions = None
    if part_two:
        starters = []
        endings = []

    for line in lines:
        if line == '\n':
            continue
        elif '=' in line:
            node, options = line.split('=')
            options = options.strip()
            node = node.strip()
            temp = options[0:1]+"'"+options[1:4]+"'"+options[4:-1]+"'"+options[-1:]
            directions = literal_eval(temp.replace(' ',"'"))
            mapping[node] = directions
            if part_two:
                if node[-1] == 'A':
                    starters.append(node)
                if node[-1] == 'Z':
                    endings.append(node)
        else:
            instructions = line.strip()
    
    if part_two:
        steps = walk_path_p2(mapping, starters, instructions, endings)
        print('The amount of steps required to reach only nodes ending with Z part two:', steps)
    else:
        steps = walk_path(mapping, 'AAA', instructions)
        print('The amount of steps required to reach ZZZ part one:', steps)
    return

def walk_path(mapping, current, instructions):

    step = 0
    reached = False
    while not reached:
        directions = mapping[current]
        if instructions[0] == 'L':
            current = directions[0]
        else:
            current = directions[1]
        
        step += 1

        if current == 'ZZZ':
            reached = True
        else:
            instructions = instructions[1:] + instructions[0]
    return step
        
def walk_path_p2(mapping, all_starters, instructions, endings):
    current_nodes  = all_starters
    step = [0] * len(all_starters)
    reached = [False] * len(all_starters)
    while False in reached:
        for i in range(0,len(current_nodes)):
            current = current_nodes[i]
            if not reached[i]:
                directions = mapping[current]
                if instructions[0] == 'L':
                    next_node = directions[0]
                else:
                    next_node = directions[1]
                
                step[i] += 1
                if next_node in endings:
                    reached[i] = True
                current_nodes[i] = next_node
            else:
                continue
        instructions = instructions[1:] + instructions[0]
    
    return lcm(*step)

wasteland()        
wasteland(True)
