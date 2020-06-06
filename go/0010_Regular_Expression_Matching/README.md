# 10. Regular Expression Matching - Hard

```
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

```

# Relative Topics
* String
* Dynamic Programming
* Backtracking

# Note
```
Time: 2020/06/07

```


# Solution
## 1. Dynamic Programming

### Intuition

As the problem has an optimal substructure, it is natural to cache intermediate results. We ask the question dp(i, j): does text[i:] and pattern[j:] match? We can describe our answer in terms of answers to questions involving smaller strings.

### Complexity Analysis
*   Time Complexity: O(TP), where T, P be the lengths of the text and the pattern respectively.
*   Space Complexity: O(TP). The only memory we use is the O(TP) boolean entries in our cache. Hence the space complexity is O(TP)