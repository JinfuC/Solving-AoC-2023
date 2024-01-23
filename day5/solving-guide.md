## Part One

In part one, the task is to transform the given numbers through several mappings and return the lowest number out of the transformed numbers.

Your first idea might be to create a dictionary to mimic the mapping, but your RAM will probably die if you attempt this method on the real input. Because if you look at the input, you'll notice that the ranges are in the millions.

What we need in part one is to map the numbers ourselves with some simple arithmetic instead of using a key value data structure.

My approach:
- Read in the file and parse it line by line. Save the initial seeds as ints and keep track of the mapping ranges of the 'mapping block' (e.g. *seed-to-soil map*)
- After processing one mapping block, apply the mapping on the seeds (I'll call every mapped thing as seeds, but actually the naming differs after each mapping like soil, fertilizer etc)
- To map it manually, check for every seed if it is within any ranges (source + range).
- If it is within a source range X. Take the difference between the destination seed and source seed of range X. This number will be the difference you need to add to your seed to map it.
- If the seed is not within any mapping ranges, the seed maps to itself.
- After processing the last mapping block, return the smallest number of your seeds.

## Part Two
 
Part two is the same as part one, but you have a lot more seeds. With that many seeds, it is impossible to map them all within a reasonable time.

The way I solved it, was to sample the initial pool with steps starting with 10^7. After each sample, I replace the initial seeds with the best 50 seeds and a range depending on the sample step. Afterwards, I reduced the sample by a factor 10 until I end up with a sample step size of one.

Initially I attempted to combine different mapping blocks together, but it got too messy so I abandoned that idea.