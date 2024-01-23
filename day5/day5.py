from copy import deepcopy

def fertilizer():

    with open('input.txt') as f:
        lines = f.readlines()
    
    # part one
    fertilizer_core(None, None, lines, False)
    # part two
    sample_steps = [pow(10,i) for i in range(7,1,-1)]
    # from input file
    initial_seeds = [629551616, 310303897, 265998072, 58091853, 3217788227, 
     563748665, 2286940694, 820803307, 1966060902, 108698829, 
     190045874, 3206262, 4045963015, 223661537, 1544688274, 
     293696584, 1038807941, 31756878, 1224711373, 133647424]
    sampled_seeds = deepcopy(initial_seeds)

    for sample_step in sample_steps:
        best_locations_so_far, best_seeds_so_far  = fertilizer_core(sampled_seeds, sample_step, lines, True)
        sampled_seeds = []
        for seed in best_seeds_so_far:
            sampled_seeds.append(seed - sample_step)
            sampled_seeds.append(sample_step * 2)

    print('Lowest location number from sampling part two:', best_locations_so_far[0])
    return

def fertilizer_core(sample_seeds, step, lines, part_two= False):
    
    seeds = []
    last_map = []
    last_header = ''

    # part two
    if part_two:
        seeds = deepcopy(sample_seeds)
    seeds_before_mappings = []

    for line in lines:
        line = line.strip()
        # first line
        if 'seeds:' in line:
            # part two
            if part_two:
                new_seeds = []
                ranges = []
                # split in ranges
                for i in range(0, len(seeds)-1, 2):
                    start, rng = seeds[i], seeds[i+1]
                    new_seeds.append(start)
                    ranges.append(rng)
                seeds = deepcopy(new_seeds)
                # sample
                for i in range(0,len(seeds)):
                    if step < 1000:
                        step = 1
                    for j in range(0, ranges[i],step):
                        seeds.append(new_seeds[i]+j)
                seeds_before_mappings = deepcopy(seeds)
            else:
                _, parsed_seeds = line.split(':')
                seeds = [int(seed) for seed in parsed_seeds.strip().split(' ')]
    
        # process the mapping block
        elif (line == '' and last_header != '') or line == lines[-1]:
            if line == lines[-1]:
                last_map.append(line.strip())
            
            new_map = [(int(src),int(rng),int(dest)) for (dest,src,rng) in (element.split(' ') for element in last_map)]
            
            new_seeds = []
            for seed in seeds:
                new_seed = None
                for src,rng,dest in new_map:
                    if seed in range(src, src+rng):
                        diff = dest - src
                        new_seed = seed + diff
                        break
                if new_seed is None:
                    new_seed = seed
                new_seeds.append(new_seed)
            seeds = deepcopy(new_seeds)
            
            last_header =''
            last_map = []
        
        # white line immediately after seeds
        elif line == '':
            continue
        # mapping block
        elif 'map:' in line:
            last_header = line.strip()
        else:
            last_map.append(line.strip())
    
    if part_two:
        # get the 100 best seeds
        sorted_seeds = sorted(seeds)
        return sorted_seeds[:50], [seeds_before_mappings[seeds.index(sorted_seed)] for sorted_seed in sorted_seeds[:50]]
    else:
        print('Lowest location number of part one:', min(seeds))

fertilizer()