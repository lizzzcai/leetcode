# 231. Power of Two - Easy

```
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false

```

# Relative Topics
* Math
* Bit Manipulation


# Note
```
Time: 2020/06/09

```


# Solution
## 1. math

### Intuition

If the num % 2 == 0 for every num /= 2, and num >= 1, then it is power of two

### Complexity Analysis
*   Time Complexity: O(1), below 32 iteration
  
*   Space Complexity: O(1)


## 2. Bit manipulation

### Intuition

Power of 2 means only one bit of n is '1', so use the trick n&(n-1)==0 to judge whether that is the case

### Complexity Analysis
*   Time Complexity: O(1)
*   Space Complexity: O(1)