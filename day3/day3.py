
def gears_first_part():

    with open('input.txt') as f:
        lines = f.readlines()
    
    matrix = {}
    symbols_dict = {}
    possible_non_numbers = {'.'}
    row = 0
    for line in lines:
        col = 0
        for char in line.strip():
            matrix[(row,col)] = char
            if char not in '0123456789.':
                symbols_dict[(row,col)] = char
                possible_non_numbers.add(char)
            col += 1
        row += 1

    total = 0

    for i in range(0,row):
        number = ''
        coordinates_of_number = []
        for j in range(0,col):
            
            element = matrix[(i,j)]
            
            if element in '0123456789':
                number += element
                coordinates_of_number.append((i,j))
            
            if ((element in possible_non_numbers) or (j+1 == col)) and number != '':
                found = False
                for coordinate_number in coordinates_of_number:
                    for symbol_coord in symbols_dict.keys():
                        if not found and is_adjacent(coordinate_number, symbol_coord):
                            total += int(number)
                            found = True
                
                number = ''
                coordinates_of_number = []
    print('sum of all part numbers:', total)
    return


def gears_second_part():
    with open('input.txt') as f:
        lines = f.readlines()
    
    matrix = {}
    gears_set = set()
    possible_non_numbers = {'.'}
    row = 0
    for line in lines:
        col = 0
        for char in line.strip():
            matrix[(row,col)] = char
            if char not in '0123456789.':
                if char == '*':
                    gears_set.add((row,col))
                possible_non_numbers.add(char)
            col += 1
        row += 1
    
    valid_gears= []

    for x,y in gears_set:
        counter = 0
        # top, same, and bot row
        for adjx in [-1,0,1]:
            # row is out of bounds
            if x+adjx  <0 or x+adjx  == row:
                continue
            # * is on left border
            if y-1 <0:
                colrange = (y,y+2)
            # * is on right border
            elif y+1 == col:
                colrange = (y-2,y)
            # * is in middle
            else:
                colrange = (y-1,y+2)
            # if top or bottom row
            if adjx == -1 or adjx == 1:
                adjacent_row = [matrix[(x+adjx, y_co)] for y_co in range(colrange[0], colrange[1])]
                if len(adjacent_row) == 3:
                    # two numbers case
                    if adjacent_row[1] == '.' and adjacent_row[0] in '0123456789' and adjacent_row[2] in '0123456789':
                        counter += 2 
                    # one number case                                                 
                    elif any((element in '0123456789' for element in adjacent_row)):
                        counter +=1
                # * on border
                else:
                    if any((element in '0123456789' for element in adjacent_row)):
                        counter += 1
            # middle row, check left and right of *
            else:
                if y-1 >= 0:
                    if matrix[(x,y-1)] in '0123456789':
                        counter +=1
                if y+1 < col:
                    if matrix[(x,y+1)] in '0123456789':
                        counter +=1
        if counter == 2:
            valid_gears.append((x,y))
                        
    total = 0
    # for every valid gear, get the adjacent numbers
    for gear in valid_gears:
        numbers = []
        for i in range(0,row):
            number = ''
            coordinates_of_number = []
            
            for j in range(0,col):
                element = matrix[(i,j)]

                if element in '0123456789':
                    number += element
                    coordinates_of_number.append((i,j))
        
                if ((element in possible_non_numbers) or (j+1 == col)) and number != '':
                    for coordinate_number in coordinates_of_number:
                        if number!= '' and is_adjacent(coordinate_number, gear):
                            numbers.append(int(number))
                            number = ''
                    number = ''
                    coordinates_of_number = []
        if len(numbers) == 2:
            total += (numbers[0] * numbers[1])
    print('Total sum of all gear ratios:', total)
    return total

def is_adjacent(nb_co, sym_co):
    # row - 1 -> row + 1 , col- 1 -> col + 1
    x1,y1 = nb_co
    x2,y2 = sym_co
    if (x1==x2 or x2-1 == x1 or x2+1 == x1) and (y1==y2 or y2-1 == y1 or y2+1 == y1):
        return True
    return False

gears_first_part()
gears_second_part()