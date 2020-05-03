'''
03/05/2020

516. Longest Palindromic Subsequence - Medium

Tag: Dynamic Programming

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

'''

from typing import List
# Solution
class Solution1:
    '''
    brute force + memoization
    Time complexity : O(n^2)
    Space complexity : O(n^2)
    '''
    def longestPalindromeSubseq(self, s: str) -> int:
        
        memo = {}
        def helper(l, r, s, memo):
            if l == r:
                return 1
            if l > r:
                return 0
            
            if (l,r) in memo:
                return memo[(l,r)]
            
            if s[l] == s[r]:
                memo[(l,r)] = 2 + helper(l+1, r-1, s, memo)
            else:
                memo[(l,r)] = max(helper(l+1, r, s, memo), helper(l, r-1, s, memo))
            
            return memo[(l,r)]
        
        
        return helper(0, len(s)-1, s, memo)


class Solution2:
    def longestPalindromeSubseq(self, s: str) -> int:
    '''
    DP
    https://leetcode.com/problems/longest-palindromic-subsequence/discuss/216717/Python-DP-solution-w-explanation
    Time complexity : O(n^2)
    Space complexity : O(n^2)
    '''
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n-1,-1,-1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][n-1]
                

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.longestPalindromeSubseq
            self.assertEqual(func("bbbab"), 4)
            self.assertEqual(func("cbbd"), 2)
            self.assertEqual(func("cbabd"), 3)
            self.assertEqual(func("c"), 1)

if __name__ == '__main__':
    unittest.main()