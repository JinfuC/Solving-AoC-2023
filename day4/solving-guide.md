## Part One

Day 4 is very much a 'advent of reading comprehension'. A tl;dr of day 4 part one is to find the amount of winning numbers within a card. The first win within a card nets you one point, and each other win doubles that one point. (Basically function points  = 2 ^ (wins - 1) )

My approach is pretty straightforward:
- Parse it line by line and separate the winning numbers and 'your' numbers.
- Use a tuple comprehension to check if a number appears in the winning numbers, if it is set the element to 1, others 0.
- Take the sum of the tuple comprehension, which will be the amount of winning numbers. If the amount is greater than zero. Add to a total points counter ```pow(2,wins-1)```

## Part Two
 
In part two, there is this chain effect of winning. I suggest to get a notepad and note down to see how this chain effect works.

For each game you have to track the amount of wins + distribute copies based on that win.

- I track the amount of copies for each game with a dictionary. Start with a dictionary with the game ids as keys and 0 as values. This dictionary will save the amount of copies for each game.
- After counting the amount of winning numbers from part 1, if the amount is greater than zero, then modify the copy dictionary for the subsequent games. 
- you want to create copies for the next x cards, where x is the amount of winning numbers in your current card. The amount of copies for card Y will be the current amount of copies of card Y + the copy we just won from this original game + the copies we won from the copies of this game.
- The final amount of cards is the sum of all copies and the amount of original cards.