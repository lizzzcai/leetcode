# 792. Number of Matching Subsequences - Medium

```
Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
Note:

All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].
```

# Relative Topics
* Array


# Note
```
Time: 2020/06/09

```


# Solution
## 1. hash table

### Intuition
iterate through each ch in S, at the same time, get the remaining string of ch in the map,
remove the ch, for each remaining string, use the first ch as key and remaining as value and append into the map. if any of the remaining string is empty, then + 1 to the result.

### Complexity Analysis
*   Time Complexity: O(len(S) + sum(len(words)))
  
*   Space Complexity: O(len(S)*len(words))