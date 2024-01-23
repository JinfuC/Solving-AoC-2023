## Part One

For part one, it is pretty straightforward. You have to check if a game is possible, given the amount of cubes. I do the following:
- Define a dictionary with the cube color as key and the the amount as value.
- Read in the file and go through it line by line. 
- Parse line by line to obtain the game id, and the different set of cubes within a game.
- Within each cube set, check the cube color and amount used, compare it to the amount in the dictionary.
- If the amount of the cube exceeds the value in the dictionary. The the amount of cubes we have is higher than the provided amount, thus this game is not possible to play.
- Before the next game (line) is analyzed, add the game id to the a counter.

## Part Two
Part two is very similar to part one, but instead of checking if the cubes exceed the given amount, you have to keep track of the max amount of cubes in each game.

Building from the solving method used in part one, some additional logic is required. I added the additional logic to the same function from part one. 
- Define a counter, which represents the power that the puzzle is asking for.
- When analyzing the games, start with an dictionary ```given_cubes = {'red':0, 'green':0, 'blue':0}```.
- If the amount of a cube exceeds the value of that cube in ```given_cubes```, change the value of that cube to that amount.
- Go through the saved values in ```given_cubes```, multiply the values, and add it to the counter.