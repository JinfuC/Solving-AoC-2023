
def cube_game(puzzle_part = 2):

    with open('input.txt') as f:
        lines = f.readlines()
    
    allowed_games_counter = 0
    given_cubes = {'red':12, 'green':13, 'blue':14}
    total_power = 0  # additional logic part 2

    for line in lines:
        game_part, cubes_used_in_game = line.split(':')
        game_id = game_part.split(' ')[-1]
        cube_sets = cubes_used_in_game.split(';')
        over_lim = False

        # additional logic part 2
        if puzzle_part == 2:
            given_cubes = {'red':0, 'green':0, 'blue':0}

        for cube_set in cube_sets:               
            for cube_in_set in cube_set.split(','):
                nb, col = cube_in_set.strip().split(' ')
                
                if int(nb) > given_cubes[col]:
                    # additional logic part 2
                    if puzzle_part == 2:
                        given_cubes[col] = int(nb)

                    else:
                        over_lim = True
    
        if not over_lim:
            allowed_games_counter += int(game_id)
        
        # additional logic part 2
        if puzzle_part == 2:
            temp_product = 1
            for v in given_cubes.values():
                temp_product *= v
            total_power += temp_product
    
    if puzzle_part == 2:
        print('sum of power:', total_power)
    else:
        print('sum of IDs:', allowed_games_counter)

    return

cube_game(1)
cube_game(2)

