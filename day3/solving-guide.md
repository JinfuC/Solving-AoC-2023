## Part One

When comparing day 3 to the previous two days, day 3's puzzle is quite challenging. In part one, you have to go through a grid and check for numbers adjacent to any symbols (excluding ```.```) and add them up.
The strategy I used consists of these steps:
- Read in the grid, I used a dictionary for it (coordinates as key and the element on that coordinate as value), but a 2D list would work as well. Additionally, keep track of the possible symbols that could be present and where they are located. For these two, I used a dictionary and a set respectively.
- Now with the grid read in, go through every row and every column to search for numbers. I keep track of numbers string a placeholder. The element gets added to it when they belong to the ```'0123456789'``` string.
- When encountering a symbol or arriving at the end of the row, check if the placeholder number that we kept track is next to any symbols. 
- If the placeholder number is next to a symbol, add it to a counter that keeps track of the total sum.

## Part Two
When building part two from the algorithm that I used in part one. I had to add a way to check whether a ```*``` is valid or not.

There are a couple ways two different numbers can be adjacent to gears (```*```). Some examples are:
```
1.1    ...    ..1
.*. or .*. or .*. or ...
...    1.1    1..
```

If you know which gears are valid, the only thing remaining is to re-adapt the algorithm from part one. Instead going through every number and check for adjacent symbols, we go through every gear and check for the two adjacent numbers.

So summarized, I did the following to solve part two:
-  Write additional logic to check whether gear is valid or not by checking the cells around ```*```.
- Re-write the algorithm to go through every valid gear and check for its adjacent numbers. For every two numbers that we find, multiply those two together and add them to a total counter.
