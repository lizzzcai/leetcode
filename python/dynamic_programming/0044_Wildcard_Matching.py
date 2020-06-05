'''
05/06/2020

44. Wildcard Matching - Hard

Tag: String, Dynamic Programming, Backtracking, Greedy

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false

'''

from typing import List
# Solution
class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        https://leetcode.com/problems/wildcard-matching/discuss/370736/Detailed-Intuition-From-Brute-force-to-Bottom-up-DP
        Top-Down DP
        recursion + memo
        Time: O(N^2)
        Space: O(N^2)
        '''
        
        def backtrack(s, p, i, j, memo):
            if (i, j) in memo:
                return memo[(i, j)]
            
            res = False
            if i == len(s) and j == len(p):
                res = True
            
            elif j == len(p):
                res = False

            elif i == len(s):
                res = p[j] == '*' and backtrack(s, p, i, j+1, memo)
            
            elif j >= len(p) or i >= len(s):
                res = False
            
            elif p[j] == '*':
                res = backtrack(s, p, i, j+1, memo) or backtrack(s, p, i+1, j, memo)
            elif p[j] == '?' or s[i] == p[j]:
                res = backtrack(s, p, i+1, j+1, memo)
            else:
                res = False
            
            memo[(i, j)] = res
            return res
        
        return backtrack(s, p, 0, 0, {})
                
                

class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        https://leetcode.com/problems/wildcard-matching/discuss/370736/Detailed-Intuition-From-Brute-force-to-Bottom-up-DP
        bottom up DP
        recursion + memo
        Time: O(N^2)
        Space: O(N^2)
        '''
        dp = [[False]*(len(p)+1)  for _ in range(len(s)+1)]

        for i in range(0, len(s)+1):
            for j in range(0, len(p)+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = p[j-1] == '*' and dp[i][j-1]
                elif j == 0:
                    dp[i][j] = False
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                elif s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
        
        return dp[len(s)][len(p)]
                

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.isMatch
            self.assertEqual(func("aa", "a"), False)
            self.assertEqual(func("aa", "*"), True)
            self.assertEqual(func("cb", "?a"), False)
            self.assertEqual(func("adceb", "*a*b"), True)
            self.assertEqual(func("acdcb", "a*c?b"), False)




if __name__ == '__main__':
    unittest.main()