# 516. Longest Palindromic Subsequence - Medium

```
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
 

Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
 

Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.
```

# Relative Topics
* Dynamic Programming



# Note
```
Time: 2020/06/09

```


# Solution
## 1. dynamic programming

### Intuition
dp[i][j] to repersent the max length of palindromic subsequence in s[i:j+1] (include i, exclude j+1)
if i == j:
dp[i][j] == 1 as s[i:j+1] is char itself

if s[i] == s[j]:
dp[i][j] = dp[i+1][j-1] + 2

if s[i] != s[j]:
dp[i][j] = max(dp[i+1][j], dp[i][j-1])


### Complexity Analysis
*   Time Complexity: O(n^2)
  
*   Space Complexity: O(n^2)