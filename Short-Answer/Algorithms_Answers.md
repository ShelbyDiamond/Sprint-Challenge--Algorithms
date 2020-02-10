#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n); because the while loop only runs n times based on variable
```python
a = 0
while (a < n * n * n):
    a = a + n * n
```


b) **O(n log n)**
* Because the inner loop is running on less than what the outer loop is
```python
sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

c) **O(n)**
* Because this runs for every bunny passed in
```python
def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

In real life, an egg would break from hardly any height so it would probably be best to start from the shortest point
and go up a floor at a time. However, in a code sense that's not the most efficient way to find something you're looking 
for. So let's say the landing area is super padded to keep the egg safe until close to terminal velocity. We'll ignore
the physics of the situation, since it could easily be calculated and floor estimated.

If I were to code this, I would start with the halfway point of the building (floor 50 for n=100) and drop the egg from 
there to get the results. From there you could continue halfway points until you find the layer where the egg breaks but
floor - 1 does not. So if you drop from the halfway point and the egg doesn't break, I'd move up to the next halfway
point (floor 75 for n=100). If it breaks, then move to the halfway point (floor 63). Since you are dividing the 
available data points in half each step, you should find the floor within log(n) steps.
