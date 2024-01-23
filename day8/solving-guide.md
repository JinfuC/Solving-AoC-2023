## Part One

Day 8 part one is a puzzle where a map data structure comes in handy.
Part one is to follow the instruction (the instruction repeats itself) of the first line of file, start in ```AAA``` and end in ```ZZZ```, check how many steps you need.

My approach for part one:
- Define an empty dictionary for all the navigation nodes.
- Read in the file and parse it line by line.
- Save the instruction in a variable.
- add navigation line to the dictionary, the node as key and the two destination nodes as a tuple as value.
- Start with current node ```AAA```, in a while loop:
    - Check the two destination nodes of the current node using the dictionary.
    - Take the correct destination node (from instruction) and assign it as the current node. Increment a step counter.
    - If the current node is ```ZZZ```, end the loop.
    - If the current node is not ```ZZZ```, shift the instruction string by one and repeat the loop.
- The total step counter is the answer for part one.

## Part Two

Part two has multiple starting nodes and you walk through them simultaneously. It asks for the amount of steps it takes to only end up in nodes ending with ```Z```.

The way to solve part two is to think about cycles. The input is crafted in such a way that for every starting node, you will reach an end node in X steps, and after X steps again, you will reach another end node. This behaviour allows us to solve part two using least common multiple.

The algorithm for part two is the same, but now you have to repeat it for multiple starting nodes. After calculating the amount of steps that each starting node needs to reach an ending node, take the least common multiple of all those steps to obtain the final answer.