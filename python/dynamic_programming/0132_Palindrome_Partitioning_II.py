'''
21/07/2020

132. Palindrome Partitioning II - Hard

Tag: Dynamic Programming

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n^2)
    Space complexity : O(n^2)
    '''
    def minCut(self, s: str) -> int:
        '''
        https://leetcode.com/problems/palindrome-partitioning-ii/discuss/42199/My-DP-Solution-(-explanation-and-code)
        '''
        if not s:
            return 0
        
        n = len(s)
        # p[i][j]: if s[i:j+1] is pal
        pal = [[False]*n for _ in range(n)]
        # dp[i]: min cut for s[i:n]
        dp = [0] * n
        
        for i in range(n-1, -1, -1):
            # set value as max cut for s[i:n]
            dp[i] = n-1-i
            
            for j in range(i, n):
                if s[i] == s[j] and (j-i < 2 or pal[i+1][j-1] == True):
                    pal[i][j] = True
                
                    if j == n-1:
                        dp[i] = 0
                    else:
                        if dp[i] > dp[j+1]+1:
                            dp[i] = dp[j+1] + 1

        
        return dp[0]

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.minCut
            self.assertEqual(func("aab"), 1)
            self.assertEqual(func("aabcc"), 2)
            self.assertEqual(func("abcde"), 4)


if __name__ == '__main__':
    unittest.main()