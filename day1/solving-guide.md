## Part One

For the first part of this fun little puzzle, I do the following:
- Read in the file and parse it line by line after stripping it. Stripping removes the '\n' character at the end of each line.
- For every line, check character per character whether they are a number or not. Save that character in case it is inside the string.
- If a number is encountered, break the character loop and start checking character per character from the end to the start of the string. If another number is encountered, break the character loop and save that character. These two saved characters are the first and last number encountered for that line.
- Both numbers are still in string format, concatenate them together and convert it to an integer. Afterwards, add this number to a counter that keeps the total sum.

## Part Two
Part two contains something tricky that you have to take into account. String numbers can overlap with eachother. Take for example the string ```eightwo```, in this string, both ```eight``` and ```two``` are present. This can be an issue if you want to implement part 2 by going through the string from front to back and update the last encountered number as you go.

Building from the solving method used in part 1, some additional logic is required.
- Instead of just checking every character, I keep the last couple characters in a variable called ```last_str```. Every character that isn't in ```'123456789'```, gets added to ```last_str```.
- I define a tuple ```possible_nb_strs = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')``` with all the possible string integers. This tuple is to check whether a string number is present in ```last_str```.
- The same algorithm is the same from part 1, but with the addition of checking for a string number in ```last_str``` after every character. For fetching the string number easily, I use the ```.index()``` built-in and add a one to it (since indexing start at 0).

### Remark

You might have noticed that when going from front to back, breaking after first encountered number, and continuing from back to front, skips the whole 'tricky' situation with overlapping string numbers. This is because you stop reading after encountering the first/last (string) number.

In case you want to read the line character per character and keep track of the last encountered number, you have to reset ```last_str``` to any possible overlap characters. e.g. After forming ```'eight'``` reset to ```'t'``` for a possible ```'eightwo'``` situation or   ```'one'``` reset to ```'e'``` for a possible ```'oneight'``` situation.