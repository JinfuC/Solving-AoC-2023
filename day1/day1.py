
def number_add_first_part():
    
    with open('input.txt') as f:
        lines = f.readlines()
    
    first_int = None
    last_int = None
    total = 0
    for line in lines:
        line = line.strip()

        for i in range(len(line)):
            if line[i] in '123456789':
                first_int = line[i]
                break
        
        for i in range(len(line)-1,-1,-1):
            if line[i] in '123456789':
                last_int = line[i]
                break

        total += int(first_int + last_int)
        first_int = None
        last_int = None
    print('total part 1:', total)
    return 

def number_add_second_part():
    first_int = None
    last_int = None
    total = 0
    possible_nb_strs = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')

    with open('input.txt') as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        last_str = ''
        
        for char in line:
            last_str += char
            any_number_in_str = [element in last_str for element in possible_nb_strs]
            if any(any_number_in_str):
                index = any_number_in_str.index(True)
                first_int = str(index+1)
                break
            elif char in '123456789':
                first_int = char
                break
        
        last_str = ''
        for char in line[::-1]:
            last_str = char + last_str
            any_number_in_str = [element in last_str for element in possible_nb_strs]
            if any(any_number_in_str):
                index = any_number_in_str.index(True)
                last_int = str(index+1)
                break
            elif char in '123456789':
                last_int = char
                break
        
        total += int(first_int + last_int)
        first_int = None
        last_int = None
        
    print('total part 2:', total)
    return

number_add_first_part()
number_add_second_part()