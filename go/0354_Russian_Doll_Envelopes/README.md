# 354. Russian Doll Envelopes - Hard

```

You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3 
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

```

# Relative Topics
* Binary Search
* Dynamic Programming


# Note
```
Time: 2020/06/09

```


# Solution
## 1. sort + LIS

### Intuition

sort it by width to asend and sort by height to descend, as under same width, only one height can be selected. we sort it in this way that we can convert the problems to find the LIS

### Complexity Analysis
*   Time Complexity: O(nlogn)
  
*   Space Complexity: O(n)
