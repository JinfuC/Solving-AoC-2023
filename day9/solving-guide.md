## Part One
Short and sweet puzzle for day 9 part one. Definitely one of the easiest ones out of the first 10 days.

- Start by reading in the file and we'll go through it line by line
- Parse the line to obtain the integer numbers of the series
- Calculate the difference series in a while loop until you arrive with a series with the same numbers (```len(set(current_series)) != 1```).
Inside this while loop:
    - Add the last value of your current series to a list ```last_value_series```.
    - The difference series is calculated by going through the values of the current series and taking the difference of two values (be careful with out of bounds indexing).
- When the while condition is satisfied, you have a list with all the last values of all the series you have calculated so far.
- Add the a value (since they are all the same) of ```current_series``` to the last element of the ```last_values_series``` list. 
- Starting from the last element of ```last_values_series```, add element -1 to element -2 and element -2 to element -3 etc.
- The first value in ```last_values_series``` contains the extrapolated value
- Keep track using a counter and add the extrapolated values together.
    


## Part Two

Since the question for part two is to do the same but backwards, which we can achieve by simply reversing our list after parsing.