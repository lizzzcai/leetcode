'''
10/06/2020

1312. Minimum Insertion Steps to Make a String Palindrome - Hard

Tag: Dynamic Programming

Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

 

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we don't need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
Example 4:

Input: s = "g"
Output: 0
Example 5:

Input: s = "no"
Output: 1
 

Constraints:

1 <= s.length <= 500
All characters of s are lower case English letters.

'''

from typing import List
# Solution
class Solution1:
    '''
    https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/discuss/470706/JavaC%2B%2BPython-Longest-Common-Sequence

    If we know the longest palindromic sub-sequence is x and the length of the string is n then, what is the answer to this problem? It is n - x as we need n - x insertions to make the remaining characters also palindrome.

    Time complexity : O(n^2)
    Space complexity : O(n^2)
    '''
    def minInsertions(self, s: str) -> int:
        
        def maxLengthPalidromeSubseq(s):
            n = len(s)
            dp = [[0]*n for _ in range(n)]
            
            for j in range(n):
                for i in range(j, -1, -1):
                    if i == j:
                        dp[i][j] = 1
                    elif s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1] + 2
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j-1])
            
            return dp[0][n-1]
        
        return len(s) - maxLengthPalidromeSubseq(s)

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.minInsertions
            self.assertEqual(func("zzazz"), 0)
            self.assertEqual(func("mbadm"), 2)
            self.assertEqual(func("leetcode"), 5)
            self.assertEqual(func("g"), 0)
            self.assertEqual(func("no"), 1)



if __name__ == '__main__':
    unittest.main()