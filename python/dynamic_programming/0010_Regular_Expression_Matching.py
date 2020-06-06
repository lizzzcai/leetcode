'''
06/06/2020

10. Regular Expression Matching - Hard

Tag: String, Dynamic Programming, Backtracking

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

'''

from typing import List
# Solution
class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        Bottom-Up
        https://leetcode.com/problems/regular-expression-matching/discuss/5651/Easy-DP-Java-Solution-with-detailed-Explanation
        
        '''
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        
        for i in range(len(s)+1):
            for j in range(len(p)+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0: # count as empty
                    dp[i][j] = p[j-1] == '*' and dp[i][j-2]
                elif j == 0: # no pattern
                    dp[i][j] = False
                elif s[i-1] == p[j-1] or p[j-1] == '.': # match or pattern = '.'
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*' and j-1 > 0:
                    if s[i-1] == p[j-2] or p[j-2] == '.': # if match
                        # can be multi, single, or emtpy
                        dp[i][j] = dp[i-1][j] or dp[i][j-1] or dp[i][j-2]
                    else: # count as empty
                        dp[i][j] = dp[i][j-2] 

        return dp[len(s)][len(p)]
                    

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.isMatch
            self.assertEqual(func("aa", "a"), False)
            self.assertEqual(func("aa", "a*"), True)
            self.assertEqual(func("ab", ".*"), True)
            self.assertEqual(func("aab", "c*a*b"), True)
            self.assertEqual(func("mississippi", "mis*is*p*."), False)
            self.assertEqual(func("a", ".*..a*"), False)




if __name__ == '__main__':
    unittest.main()