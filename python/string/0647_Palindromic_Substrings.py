'''
03/05/2020

647. Palindromic Substrings - Medium

Tag: String, Dynamic Programming

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Note:

The input string length won't exceed 1000.

'''

from typing import List
# Solution
class Solution1:
    def countSubstrings(self, s: str) -> int:
        '''
        O(n^2)
        space O(1)
        '''
        def expand(i, j):
            res = 0
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    res += 1
                    i -= 1
                    j += 1
                else:
                    break
            return res
                
        
        n = len(s)
        res = 0
        for i in range(n):
            # case 1
            res += expand(i,i)
            
            # case 2
            if i < n-1:
                res += expand(i,i+1)
        
        return res
                
class Solution2:
    '''
    Manacher's Algorithm
    O(N) time
    '''
    def countSubstrings(self, s: str) -> int:
        def manachers(S):
            A = '@#' + '#'.join(S) + '#$'
            Z = [0] * len(A)
            
            center = right = 0
            for i in range(1, len(A)-1):
                if i < right:
                    Z[i] = min(right-i, Z[2 * center - i])
                while A[i+Z[i]+1] == A[i-Z[i]-1]:
                    Z[i] += 1
                if i + Z[i] > right:
                    center, right = i, i + Z[i]
            
            return Z
        
        return sum((v+1)//2 for v in manachers(s))
            
                  

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.countSubstrings
            self.assertEqual(func("abc"), 3)
            self.assertEqual(func("aaa"), 6)

if __name__ == '__main__':
    unittest.main()