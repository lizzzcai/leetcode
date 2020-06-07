# 406. Queue Reconstruction by Height - Medium

```
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

 
Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
```

# Relative Topics
* Greedy


# Note
```
Time: 2020/06/07

```


# Solution
## 1. Sort + insert

### Intuition

We sort the array from tallest to shortest, and for people with same height, we sort it by the k value(asending).
As for each person, it only count the person taller than or euqal to him, so we can insert it to a queue as the people shorter that current is not in the cretira of k value.

### Complexity Analysis
*   Time Complexity: O(N^2), where N is the length of array. insert into array take O(n)
  
*   Space Complexity: O(N)