## Part One

The puzzle for day 6 is one of my favorites of 2023. Why you ask? Because I felt really smart when I solved it.

My approach is to see the puzzle as a math problem. The mathematical function ```d(t) = t * (allowed time - t)``` corresponds to the distance function of the boat.
The problem is to find all ```t``` where ``d(t) > record distance``. If you are familiar with quadratic equations, the problem boils down to finding the roots of a quadratic equation ```ax^2 + bx + c = 0```. The roots of a quadratic equation are ```x1 = -b+D/2a and x2 = -b+D/2a with D = b^2-4ac ```

For us the quadratic equation to solve is
```-t^2 + allowed time * t - record distance > 0```. If we fill it in the general equation, this corresponds to ```a = -1, b = allowed time, c = - record distance```.

Enough math for now, let's go over the steps:
- Read in the file and parse the times and distances. Put them in data structure so you can get the time of a race and its record distance easily. I chose two lists for this.
- For every race, calculate the roots with ```a = -1, b = allowed time, c = - record distance```.
- The roots we just found are the times where we reached the record distance but didn't break the record. So we have to check all ```t``` if it is between those two roots.
- Another observation is that the time is discrete and limited. This allows us to only to focus the integers between ```t1``` and ```t2```
- Keep track of a total product using a counter.


## Part Two
 
The only thing you need to do for part two is concatenate the times and distances. If that's done, you can re-use the same algorithm from part one.