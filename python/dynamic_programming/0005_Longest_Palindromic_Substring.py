'''
05/05/2020

5. Longest Palindromic Substring - Medium

Tag: String, Dynamic Programming

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n^2)
    Space complexity : O(1)
    '''
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j, s):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i-= 1
                j += 1
            return i+1, j-1
        
        max_size = 0
        res = ""
        for i in range(len(s)):
            # case 1
            m, n = expand(i,i,s)
            if n-m+1 > max_size:
                max_size = n-m+1
                res = s[m:n+1]
            
            # case 2
            if i < len(s)-1 and s[i]==s[i+1]:
                m,n = expand(i,i+1,s)
                if n-m+1 > max_size:
                    max_size = n-m+1
                    res = s[m:n+1]
                    
                    
        return res

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.longestPalindrome
            self.assertEqual(func("babad"), "bab")
            self.assertEqual(func("cbbd"), "bb")

if __name__ == '__main__':
    unittest.main()