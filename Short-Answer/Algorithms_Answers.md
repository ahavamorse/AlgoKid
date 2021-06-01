#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime is O(n) because each time n^2 is added, and the loop repeats n^3 which 
    is n * n^2. Thus, n^2 must be added to a n times before being equal to n^3.


b) Runtime is O(n log n) because the outer loop runs in O(n) time while the inner 
    loop has a run time of log n. We know this because the j doubles each time.


c) Runtime would be O(n) because each time the same function is called once with a 
    number that is lower by 1 until 0 is reached.

## Exercise II

The best way to find the floor number at which eggs begin breaking is by dropping an 
egg halfway up the building. Then if it breaks, move down to halfway between where you 
were and the ground, or if it doesn't break then move up to halfway between where you 
were and the top of the building. Then repeat these steps. Each time move to the halfway 
point of the range you've found. At first this range will be the whole building, then 
half the building, then a quarter, each time cutting the total number of possible floors 
in half. This will result in a runtime complexity of O(log n).