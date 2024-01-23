## Part One

The puzzle for day 7 is not necessarily hard, but it takes a while to code. I'll split day 7 part one in two main parts and we'll solve it divide and conquer style.

### Determining the hands
Before we can start with everything, let's see how to determine the hand. I used a dictionary data structure. The keys of this dictionary will be the different cards and the values the amount of the cards. Given the cards and their amounts, we can determine the hand using a simple switch logic. Since there are 7 different different hands, I indicate them with numbers 0-6. 0 representing high card and 6 representing five of a kind, corresponding to the ranking given in the puzzle instructions. 
The following snippet is the logic written in pseudocode. For the real code, please refer to the code.
```
If we have five different cards -> return 0 # High card
If we all cards are the same -> return 6 # five of a kind
If a card appears 4 times -> return 5 # four of a kind
If a card appears 3 times: 
    if we only have two different cards -> return 4 # full house
    else -> return 3 # three of a kind
else (pairs):
    for amount in card_amounts:
        if amount == 2 -> add to pairs counter
    if pairs counter == 2 -> return 2 # two pairs
    else -> return 1 # one pair
```

### Comparing the hands
Once we know the hand type, we still need a way to tell how strong a hand is compared to the other hands within the same type. I wrote a custom sorting function for this task, you can provide a custom sorting function in the ```key``` argument of the built-in ``` sorted()```. The custom sorting function takes two hands (in str) as arguments and goes through each card to compare which of the two hands is the better one, skipping the card if it is the same.

After writing the code for these two features, we can now go over the algorithm to solve this puzzle:
- Parse the file and read in line by line (hands)
- For each hand, determine the type and keep track of all the hands of a certain type using a dictionary.
- Also keep track how many hands there are in total to determine the rank later
- Now, for each hand type, sort the hands by strength using the custom sorting function. Start at the strongest hand type.
- After sorting each hand type, calculate the winnings of each hand using the rank.
- Keep track of the total winnings using a counter.

## Part Two
 
Part two took quite some time to implement. The modification to part two, is to add a function that transforms the wildcards in a hand to obtain the best hand possible. The tansforming function logic I implemented is the following:
- In a hand, determine the cards that are not ```J``` and the amount of each card.
- Order the cards types in your hand from highest to lowest.
- If you have 5 ```J```s -> return ```AAAAA```
- If you have 4 or 3 ```J```s -> this means that you can either make five or four of a kind, replace the ```J```s with the highest card type in your hand to obtain five/four of a kind.
- If you have 2 ```J```s -> 
    - If you only have one type of card or you have three types of cards -> replace the ```J```s with the highest card to obtain five of a kind or full house or three of a kind.
    - If you have two types of cards -> replace ```J``` with the card that appears twice in your hand to obtain full house or three of a kind.
- If you have 1 ```J``` ->
    - If you only have one type of card or you have four types of cards -> replace the ```J```s with the highest card to obtain five of a kind or one pair.
    - If you have two types of cards, check which one of those two appears three times, replace the ```J``` with that card. If both appears twice in your hand, replace ```J``` with the highest card. This will result either in four of a kind or full house or three of a kind.
    - If you have three types of cards, one of them has to appear twice in your hand, so replace ```J``` with the card that appears twice in your hand to obtain full house or three of a kind.
- As you can see, in a lot of cases you replace ```J``` with the best card type, so you can rewrite the above logic in fewer lines.

Another small modification that should be made for part two is the card sorting function. Modify it so that it will rank the hands within a hand type with the new value of ```J```.

After these two modifications, add them to the algorithm of part one.

