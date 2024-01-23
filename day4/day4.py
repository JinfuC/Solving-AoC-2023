
def scratchcards():

    with open('input.txt') as f:
        lines = f.readlines()
    
    total = 0
    # part 2
    copies = {}
    for i in range(1,len(lines)+1):
        copies[i] = 0

    for line in lines:
        winning_nbs, your_nbs = line.split('|')
        your_nbs = your_nbs.strip().split(' ')
        game_info, winning_nbs = winning_nbs.strip().split(':')
        winning_nbs = winning_nbs.split(' ')
        # part 2
        game_nb = int(game_info.split('Card')[1].strip())
        
        your_nbs = tuple(filter(lambda x: x != '', your_nbs))
        winning_nbs = tuple(filter(lambda x: x != '', winning_nbs))

        wins = sum((1 if nb in winning_nbs else 0 for nb in your_nbs))

        if wins > 0:
            total += pow(2,wins-1)
            # part 2
            for i in range(game_nb+1,game_nb+wins+1):
                copies[i] = copies[i] + 1 + copies[game_nb]

    print('Total points part one:', total)
    print('Total copies part two:', sum(copies.values()) + len(lines))
    return total

scratchcards()
